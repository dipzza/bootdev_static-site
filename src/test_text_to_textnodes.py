import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
  def test_all_node_types(self):
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    result = text_to_textnodes(text)
    expected = [
      TextNode("This is ", TextType.TEXT),
      TextNode("text", TextType.BOLD),
      TextNode(" with an ", TextType.TEXT),
      TextNode("italic", TextType.ITALIC),
      TextNode(" word and a ", TextType.TEXT),
      TextNode("code block", TextType.CODE),
      TextNode(" and an ", TextType.TEXT),
      TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
      TextNode(" and a ", TextType.TEXT),
      TextNode("link", TextType.LINK, "https://boot.dev"),
    ]
    self.assertEqual(result, expected)


  def test_close_and_repeating(self):
    text = "**Bold***italic* and ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)![obi wan image 2](https://i.imgur.com/fJRm4Vk.jpeg)"
    result = text_to_textnodes(text)
    expected = [
      TextNode("Bold", TextType.BOLD),
      TextNode("italic", TextType.ITALIC),
      TextNode(" and ", TextType.TEXT),
      TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
      TextNode("link", TextType.LINK, "https://boot.dev"),
      TextNode("obi wan image 2", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
    ]
    self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()