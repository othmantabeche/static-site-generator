from HTMLNode import HTMLNode
from LeafNode import LeafNode
from ParentNode import ParentNode
from TextNode import TextNode


def main():
    text_node = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(repr(text_node))
    print("**************************************")
    html_node = HTMLNode(
        tag="a",
        value="This is some anchor text",
        props={"href": "https://www.boot.dev"},
    )
    print(repr(html_node))
    print("**************************************")
    leaf_node = LeafNode(
        tag="a",
        value="This is some anchor text",
        props={"href": "https://www.boot.dev"},
    )
    print(repr(leaf_node))
    print("**************************************")
    parent_node = ParentNode(tag="p", children=[leaf_node], props=None)
    print(repr(parent_node))


if __name__ == "__main__":
    main()
