import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def setUp(self):
      child = HTMLNode(value="raw text")
      props = {
        "href": "https://www.dipzza.es",
        "target": "_blank"
      }
      self.node = HTMLNode("h1", "Title", [child], props)
    
    def test_props_to_html(self):
        expected = ' href="https://www.dipzza.es" target="_blank"'
        self.assertEqual(self.node.props_to_html(), expected)

    def test_empty_props_to_html(self):
        node = HTMLNode("h1", "Title")
        expected = ""
        self.assertEqual(node.props_to_html(), expected)
    
    def test_repr(self):
        expected = ("Tag: h1, Value: Title, Children: [Tag: None, Value: raw text,"
                    " Children: None, Props: None], Props: "
                    "{'href': 'https://www.dipzza.es', 'target': '_blank'}")
        self.assertEqual(repr(self.node), expected)

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode('h1', "raw text", { "href": "url.es"})
        expected = '<h1 href="url.es">raw text</h1>'
        self.assertEqual(node.to_html(), expected)
    
    def test_to_html_no_tag(self):
        node = LeafNode(None, "raw text")
        expected = "raw text"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_bad_value(self):
        node = LeafNode('h1', None)
        self.assertRaises(ValueError, node.to_html)

class TestParentNode(unittest.TestCase):
    def setUp(self):
        self.leafchild = LeafNode('b', 'bold text', None)
        self.leafchild2 = LeafNode('i', 'italic text', None)


    def test_to_html(self):
        subParent = ParentNode("a", [self.leafchild, self.leafchild2], {
            "href": "https://www.dipzza.es",
        })
        node = ParentNode("p", [subParent])
        expected = ('<p><a href="https://www.dipzza.es">'
                    '<b>bold text</b><i>italic text</i>'
                    '</a></p>')
        self.assertEqual(node.to_html(), expected)
    
    def test_to_html_no_tag(self):
        node = ParentNode(None, [self.leafchild])
        self.assertRaisesRegex(ValueError, "No tag", node.to_html)

    def test_to_html_bad_value(self):
        node = ParentNode("h1", None)
        self.assertRaisesRegex(ValueError, "No children", node.to_html)



if __name__ == "__main__":
    unittest.main()