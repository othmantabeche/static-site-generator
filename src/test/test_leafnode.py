import unittest

from LeafNode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node1 = LeafNode("p", "Hello world", {"class": "text"})
        node2 = LeafNode("p", "Hello world", {"class": "text"})
        self.assertEqual(node1, node2)

    def test_tag_not_eq(self):
        node1 = LeafNode("h1", "Hello world")
        node2 = LeafNode("p", "Hello world")
        self.assertNotEqual(node1, node2)

    def test_value_not_eq(self):
        node1 = LeafNode("p", "Hello world")
        node2 = LeafNode("p", "Goodbye world")
        self.assertNotEqual(node1, node2)

    def test_props_not_eq(self):
        node1 = LeafNode("a", "Click me", {"href": "https://example.com"})
        node2 = LeafNode("a", "Click me", {"href": "https://google.com"})
        self.assertNotEqual(node1, node2)

    def test_not_eq_other_type(self):
        node = LeafNode("p", "Hello")
        self.assertNotEqual(node, "Hello")


if __name__ == "__main__":
    unittest.main()
