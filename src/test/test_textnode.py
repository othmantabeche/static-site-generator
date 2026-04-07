import unittest

from TextNode import (
    TextNode,
    TextType,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_node_to_html_node,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_text_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)

    def test_type_not_eq(self):
        node1 = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_url_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "www.nike.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.apple.com")
        self.assertNotEqual(node1, node2)

    def test_url_none_not_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "www.apple.com")
        self.assertNotEqual(node1, node2)

    def test_not_eq_other_type(self):
        node = TextNode("Hello", TextType.TEXT)
        self.assertNotEqual(node, "Hello")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_delimiter_split(self):
        node1 = TextNode("Hello, world!", TextType.TEXT)
        node2 = TextNode("Hello, world!", TextType.BOLD)
        old_nodes = [node1, node2]
        new_nodes = split_nodes_delimiter(old_nodes, ",", TextType.TEXT)
        expected_nodes = [
            TextNode("Hello", TextType.TEXT),
            TextNode(",", TextType.TEXT),
            TextNode(" world!", TextType.TEXT),
            TextNode("Hello, world!", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_delimiter_split_no_delimiter(self):
        node1 = TextNode("Hello world!", TextType.TEXT)
        old_nodes = [node1]
        new_nodes = split_nodes_delimiter(old_nodes, ",", TextType.TEXT)
        expected_nodes = [TextNode("Hello world!", TextType.TEXT)]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("This is text with no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(
            [TextNode("This is text with no images", TextType.TEXT)], new_nodes
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com) and another [second link](https://www.apple.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://www.apple.com"),
            ],
            new_nodes,
        )


if __name__ == "__main__":
    unittest.main()
