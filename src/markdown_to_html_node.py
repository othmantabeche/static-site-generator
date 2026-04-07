import re

from markdown_to_blocks import BlockType, block_to_block_type, markdown_to_blocks
from ParentNode import ParentNode
from TextNode import TextNode, TextType, text_node_to_html_node, text_to_textnodes


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def paragraph_to_html_node(block):
    text = " ".join(block.split("\n"))
    return ParentNode("p", text_to_children(text))


def heading_to_html_node(block):
    level = len(block) - len(block.lstrip("#"))
    text = block[level:].strip()
    return ParentNode(f"h{level}", text_to_children(text))


def code_to_html_node(block):
    lines = block.split("\n")
    code_text = "\n".join(lines[1:-1])
    if code_text:
        code_text += "\n"
    code_text_node = TextNode(code_text, TextType.TEXT)
    code_leaf = text_node_to_html_node(code_text_node)
    code_node = ParentNode("code", [code_leaf])
    return ParentNode("pre", [code_node])


def quote_to_html_node(block):
    lines = block.split("\n")
    cleaned_lines = [line[1:].lstrip() for line in lines]
    text = " ".join(cleaned_lines)
    return ParentNode("blockquote", text_to_children(text))


def unordered_list_to_html_node(block):
    items = []
    for line in block.split("\n"):
        text = line[2:]
        items.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ul", items)


def ordered_list_to_html_node(block):
    items = []
    for line in block.split("\n"):
        text = re.sub(r"^\d+\.\s+", "", line)
        items.append(ParentNode("li", text_to_children(text)))
    return ParentNode("ol", items)


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    if block_type == BlockType.CODE:
        return code_to_html_node(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    if block_type == BlockType.UNORDERED_LIST:
        return unordered_list_to_html_node(block)
    if block_type == BlockType.ORDERED_LIST:
        return ordered_list_to_html_node(block)

    raise ValueError(f"Unsupported block type: {block_type}")


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", children)
