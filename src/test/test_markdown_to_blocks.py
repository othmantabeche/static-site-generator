import unittest

from markdown_to_blocks import markdown_to_blocks


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


if __name__ == "__main__":
    unittest.main()
