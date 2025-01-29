import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "link.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "link.com")
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, Text, https://www.boot.dev)", repr(node)
        )



if __name__ == "__main__":
    unittest.main()