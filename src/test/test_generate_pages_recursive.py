import os
import tempfile
import unittest

from generate_page import generate_pages_recursive


class TestGeneratePagesRecursive(unittest.TestCase):
    def test_generate_pages_recursive(self):
        template = "<html><head><title>{{ Title }}</title></head><body>{{ Content }}</body></html>"

        with tempfile.TemporaryDirectory() as tmp_dir:
            content_dir = os.path.join(tmp_dir, "content")
            nested_dir = os.path.join(content_dir, "blog")
            dest_dir = os.path.join(tmp_dir, "public")
            template_path = os.path.join(tmp_dir, "template.html")

            os.makedirs(nested_dir, exist_ok=True)

            root_markdown_path = os.path.join(content_dir, "index.md")
            nested_markdown_path = os.path.join(nested_dir, "post.md")

            with open(root_markdown_path, "w") as root_file:
                root_file.write("# Home\n\nWelcome home.")

            with open(nested_markdown_path, "w") as nested_file:
                nested_file.write("# Post\n\nThis is a _post_.")

            with open(template_path, "w") as template_file:
                template_file.write(template)

            generate_pages_recursive(content_dir, template_path, dest_dir, "/")

            root_output_path = os.path.join(dest_dir, "index.html")
            nested_output_path = os.path.join(dest_dir, "blog", "post.html")

            self.assertTrue(os.path.exists(root_output_path))
            self.assertTrue(os.path.exists(nested_output_path))

            with open(root_output_path, "r") as root_output_file:
                root_output = root_output_file.read()
            with open(nested_output_path, "r") as nested_output_file:
                nested_output = nested_output_file.read()

            self.assertEqual(
                root_output,
                "<html><head><title>Home</title></head><body><div><h1>Home</h1><p>Welcome home.</p></div></body></html>",
            )
            self.assertEqual(
                nested_output,
                "<html><head><title>Post</title></head><body><div><h1>Post</h1><p>This is a <i>post</i>.</p></div></body></html>",
            )


if __name__ == "__main__":
    unittest.main()
