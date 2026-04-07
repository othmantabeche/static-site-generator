import enum
import re


class BlockType(enum.Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown) -> list:
    blocks = markdown.strip().split("\n\n")
    result = []
    for block in blocks:
        block = block.strip()
        if block != "":
            result.append(block)
    return result


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")

    if re.match(r"^#{1,6}\s+", block):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    ordered_list_match = True
    for index, line in enumerate(lines, start=1):
        if not re.match(rf"^{index}\.\s+", line):
            ordered_list_match = False
            break
    if ordered_list_match:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
