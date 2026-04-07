import unittest

from extract_markdown_links import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.google.com)"
        )
        self.assertEqual([("link", "https://www.google.com")], matches)


if __name__ == "__main__":
    unittest.main()
