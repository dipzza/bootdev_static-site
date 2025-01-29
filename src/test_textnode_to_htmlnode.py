import unittest
from htmlnode import LeafNode
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text_conversion(self):
        node = TextNode("Hello", TextType.TEXT)
        expected = LeafNode(None, "Hello")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_bold_conversion(self):
        node = TextNode("Bold Text", TextType.BOLD)
        expected = LeafNode("b", "Bold Text")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_italic_conversion(self):
        node = TextNode("Italic Text", TextType.ITALIC)
        expected = LeafNode("i", "Italic Text")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_code_conversion(self):
        node = TextNode("print('Hello')", TextType.CODE)
        expected = LeafNode("code", "print('Hello')")
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_link_conversion(self):
        node = TextNode("Dipzza", TextType.LINK, "https://dipzza.es")
        expected = LeafNode("a", "Dipzza", {"href": "https://dipzza.es"})
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_image_conversion(self):
        node = TextNode("An example image", TextType.IMAGE, "https://example.com/image.jpg")
        expected = LeafNode("img", "", {"src": "https://example.com/image.jpg", "alt": "An example image"})
        self.assertEqual(text_node_to_html_node(node), expected)

    def test_invalid_text_type(self):
        node = TextNode("Some text", "bad type")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)