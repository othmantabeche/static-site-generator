import unittest

from HTMLNode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        node2 = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        self.assertEqual(node1, node2)

    def test_tag_not_eq(self):
        node1 = HTMLNode("h1", "Hello world")
        node2 = HTMLNode("p", "Hello world")
        self.assertNotEqual(node1, node2)

    def test_value_not_eq(self):
        node1 = HTMLNode("p", "Hello world")
        node2 = HTMLNode("p", "Goodbye world")
        self.assertNotEqual(node1, node2)

    def test_props_not_eq(self):
        node1 = HTMLNode("a", "Click me", None, {"href": "https://example.com"})
        node2 = HTMLNode("a", "Click me", None, {"href": "https://google.com"})
        self.assertNotEqual(node1, node2)

    def test_children_not_eq(self):
        child1 = HTMLNode("span", "child")
        child2 = HTMLNode("span", "different child")
        node1 = HTMLNode("div", None, [child1], None)
        node2 = HTMLNode("div", None, [child2], None)
        self.assertNotEqual(node1, node2)

    def test_not_eq_other_type(self):
        node = HTMLNode("p", "Hello")
        self.assertNotEqual(node, "Hello")


if __name__ == "__main__":
    unittest.main()
