from enum import Enum


class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"


class TextNode:
    def __init__(self, text, text_type, url):
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
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
