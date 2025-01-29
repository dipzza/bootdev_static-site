import re
import unittest

from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodes(unittest.TestCase):
    def test_split_code(self):
      node = TextNode("Text `code` and", TextType.TEXT)
      node2 = TextNode("some more `code`", TextType.TEXT)
      
      result = split_nodes_delimiter([node, node2], "`", TextType.CODE)

      expected = [
        TextNode("Text ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" and", TextType.TEXT),
        TextNode("some more ", TextType.TEXT),
        TextNode("code", TextType.CODE),
      ]
      self.assertEqual(result, expected)

    def test_split_consecutive_delimiters(self):
      node = TextNode("Text **bold****some more bold**", TextType.TEXT)

      result = split_nodes_delimiter([node], "**", TextType.BOLD)

      expected = [
        TextNode("Text ", TextType.TEXT),
        TextNode("bold", TextType.BOLD),
        TextNode("some more bold", TextType.BOLD),
      ]
      self.assertEqual(result, expected)
    
    def test_wrong_delimiter_sintax(self):
      node = TextNode("Text *italic", TextType.TEXT)
      with self.assertRaisesRegex(Exception, re.escape('Delimiter "*" mismatch on "Text *italic"')):
         split_nodes_delimiter([node], "*", TextType.ITALIC)

    def test_no_conversion_needed(self):
      node = TextNode("Text ", TextType.TEXT)
      node2 = TextNode("code", TextType.CODE)

      result = split_nodes_delimiter([node, node2], "`", TextType.CODE)

      expected = [
        TextNode("Text ", TextType.TEXT),
        TextNode("code", TextType.CODE),
      ]
      self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()