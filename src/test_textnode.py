import unittest

from TextNode import TextNode, TextType, split_nodes_delimiter, text_node_to_html_node


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


if __name__ == "__main__":
    unittest.main()
