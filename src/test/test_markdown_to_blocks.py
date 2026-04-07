import unittest

from markdown_to_blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = (
            "This is a block.\n\nThis is another block.\n\n\nThis is yet another block."
        )
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            [
                "This is a block.",
                "This is another block.",
                "This is yet another block.",
            ],
            blocks,
        )

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)
        self.assertEqual(
            block_to_block_type("- Unordered list item"), BlockType.UNORDERED_LIST
        )
        self.assertEqual(
            block_to_block_type("1. Ordered list item"), BlockType.ORDERED_LIST
        )
        self.assertEqual(block_to_block_type("```\nCode block\n```"), BlockType.CODE)
        self.assertEqual(
            block_to_block_type("This is a paragraph."), BlockType.PARAGRAPH
        )


if __name__ == "__main__":
    unittest.main()
