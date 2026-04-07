import os
import tempfile
import unittest

from generate_page import generate_page


class TestGeneratePage(unittest.TestCase):
    def test_generate_page(self):
        markdown = """# Hello World

This is a **test**.
"""
        template = """<html><head><title>{{ Title }}</title></head><body>{{ Content }}</body></html>"""

        with tempfile.TemporaryDirectory() as tmp_dir:
            from_path = os.path.join(tmp_dir, "content.md")
            template_path = os.path.join(tmp_dir, "template.html")
            dest_path = os.path.join(tmp_dir, "public", "index.html")

            with open(from_path, "w") as markdown_file:
                markdown_file.write(markdown)

            with open(template_path, "w") as template_file:
                template_file.write(template)

            generate_page(from_path, template_path, dest_path, "/")

            self.assertTrue(os.path.exists(dest_path))
            with open(dest_path, "r") as output_file:
                output = output_file.read()

            self.assertEqual(
                output,
                "<html><head><title>Hello World</title></head><body><div><h1>Hello World</h1><p>This is a <b>test</b>.</p></div></body></html>",
            )


if __name__ == "__main__":
    unittest.main()
