from HTMLNode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

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
        return f"LeafNode({self.tag!r}, {self.value!r}, {self.props!r})"

    def to_html(self):
        if self.value is None:
            raise ValueError("A leaf nodes must have a value")

        if self.tag is None:
            return self.value

        props_html = self.props_to_html()
        if props_html:
            return f"<{self.tag} {props_html}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
