from HTMLNode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=None)

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return f"ParentNode({self.tag!r}, {self.children!r}, {self.props!r})"

    def to_html(self):
        if self.tag is None:
            raise ValueError("A parent node must have a tag")

        if self.children is None:
            raise ValueError("A parent node must have children")

        props_html = self.props_to_html()
        children_html = "".join([child.to_html() for child in self.children])
        if props_html:
            return f"<{self.tag} {props_html}>{children_html}</{self.tag}>"
        return f"<{self.tag}>{children_html}</{self.tag}>"
