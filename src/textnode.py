from enum import Enum
import re

from LeafNode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text  # The text content of the node
        self.text_type = text_type  # The type of text this node contains, which is a member of the TextType enum.
        self.url = url  # The URL of the link or image, if the text is a link. Default to None if nothing is passed in.

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text!r}, {self.text_type!r}, {self.url!r})"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode(tag="img", value="", props={"src": text_node.url})
    else:
        raise ValueError(f"Unsupported text type: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == text_type:
            split_text = node.text.split(delimiter)
            for i, text in enumerate(split_text):
                if text:
                    new_nodes.append(TextNode(text, text_type))
                if i < len(split_text) - 1:
                    new_nodes.append(TextNode(delimiter, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        current_index = 0
        for match in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", node.text):
            if match.start() > current_index:
                new_nodes.append(
                    TextNode(node.text[current_index : match.start()], TextType.TEXT)
                )
            new_nodes.append(TextNode(match.group(1), TextType.IMAGE, match.group(2)))
            current_index = match.end()

        if current_index < len(node.text):
            new_nodes.append(TextNode(node.text[current_index:], TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        current_index = 0
        for match in re.finditer(r"(?<!!)\[([^\]]*)\]\(([^)]+)\)", node.text):
            if match.start() > current_index:
                new_nodes.append(
                    TextNode(node.text[current_index : match.start()], TextType.TEXT)
                )
            new_nodes.append(TextNode(match.group(1), TextType.LINK, match.group(2)))
            current_index = match.end()

        if current_index < len(node.text):
            new_nodes.append(TextNode(node.text[current_index:], TextType.TEXT))
    return new_nodes
