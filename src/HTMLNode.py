class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = (
            tag  # string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        )
        self.value = value  # string representing the value of the HTML tag (e.g. the text inside a paragraph)
        self.children = (
            children  # list of HTMLNode objects representing the children of this node
        )
        self.props = props  # dictionary of key-value pairs representing the attributes of the HTML tag

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return (
            f"HTMLNode({self.tag!r}, {self.value!r}, {self.children!r}, {self.props!r})"
        )

    def to_html(self):
        raise NotImplementedError("Not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""

        res = ""
        for i in self.props:
            res += f'{i}="{self.props[i]}" '
        return res


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)
