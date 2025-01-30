import unittest

from htmlnode import LeafNode, ParentNode
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownFunctions(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = """
## This is a heading

This is a paragraph of text. It has some *italic* words inside of it.

```
This is a code block
```

> This is a quote block with some **bold**

* This is the first list item in an unordered list
* This is another list item

1. This is the first list item in an ordered list
2. This is another list item
"""

        html_node = markdown_to_html_node(markdown)
        
        self.assertEqual(html_node.tag, "div")
        
        self.assertEqual(html_node.children[0].tag, "h2")
        self.assertEqual(html_node.children[0].children, [LeafNode(None, "This is a heading")])
        
        self.assertEqual(html_node.children[1].tag, "p")
        self.assertEqual(html_node.children[1].children, [
            LeafNode(None, "This is a paragraph of text. It has some "), 
            LeafNode("i", "italic"), 
            LeafNode(None, " words inside of it.")
            ])
        
        self.assertEqual(html_node.children[2].tag, "pre")
        self.assertEqual(html_node.children[2].children, [
            ParentNode("code", [
                LeafNode(None, "This is a code block")
              ]
            )
          ])
        
        self.assertEqual(html_node.children[3].tag, "blockquote")
        self.assertEqual(html_node.children[3].children, [LeafNode(None, "This is a quote block with some "), LeafNode("b", "bold")])
        
        self.assertEqual(html_node.children[4].tag, "ul")
        self.assertEqual(len(html_node.children[4].children), 2)  # Two list items
        self.assertEqual(html_node.children[4].children[0].tag, "li")
        self.assertEqual(html_node.children[4].children[0].children, [LeafNode(None, "This is the first list item in an unordered list")])
        self.assertEqual(html_node.children[4].children[1].tag, "li")
        self.assertEqual(html_node.children[4].children[1].children, [LeafNode(None, "This is another list item")])
        
        self.assertEqual(html_node.children[5].tag, "ol")
        self.assertEqual(len(html_node.children[5].children), 2)  # Two list items
        self.assertEqual(html_node.children[5].children[0].tag, "li")
        self.assertEqual(html_node.children[5].children[0].children, [LeafNode(None, "This is the first list item in an ordered list")])
        self.assertEqual(html_node.children[5].children[1].tag, "li")
        self.assertEqual(html_node.children[5].children[1].children, [LeafNode(None, "This is another list item")])

        self.assertEqual(len(html_node.children), 6)

if __name__ == "__main__":
    unittest.main()