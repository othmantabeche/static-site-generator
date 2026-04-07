import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = """# My Title"""
        self.assertEqual(extract_title(markdown), "My Title")

    def test_extract_title_with_extra_whitespace(self):
        markdown = """#    My Title   """
        self.assertEqual(extract_title(markdown), "My Title")

    def test_extract_title_with_multiple_lines(self):
        markdown = """# My Title
        This is some content."""
        self.assertEqual(extract_title(markdown), "My Title")

    def test_extract_title_with_no_title(self):
        markdown = """This is some content without a title."""
        with self.assertRaises(ValueError):
            extract_title(markdown)


if __name__ == "__main__":
    unittest.main()
