import re
import unittest

from split_nodes import split_nodes_delimiter, split_nodes_images, split_nodes_links
from textnode import TextNode, TextType

class TestSplitBaseNodes(unittest.TestCase):
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

class TestSplitNodesImages(unittest.TestCase):
  def test_empty_list(self):
      result = split_nodes_images([])
      self.assertEqual(result, [])
  
  def test_no_images_and_non_splittable(self):
      node = TextNode("Hello world", TextType.TEXT)
      node2 = TextNode("code", TextType.CODE)
      result = split_nodes_images([node, node2])
      self.assertEqual(result, [node, node2])
  
  def test_single_image(self):
      node = TextNode("Hello ![alt](link) world", TextType.TEXT)
      result = split_nodes_images([node])
      expected = [
          TextNode("Hello ", TextType.TEXT),
          TextNode("alt", TextType.IMAGE, "link"),
          TextNode(" world", TextType.TEXT)
      ]
      self.assertEqual(result, expected)

  def test_multiple_images(self):
    node = TextNode(
        "Start ![alt1](link1) middle ![alt2](link2) end", 
        TextType.TEXT
    )
    result = split_nodes_images([node])
    expected = [
        TextNode("Start ", TextType.TEXT),
        TextNode("alt1", TextType.IMAGE, "link1"),
        TextNode(" middle ", TextType.TEXT),
        TextNode("alt2", TextType.IMAGE, "link2"),
        TextNode(" end", TextType.TEXT)
    ]
    self.assertEqual(result, expected)

class TestSplitNodesLinks(unittest.TestCase):
  def test_empty_list(self):
      result = split_nodes_links([])
      self.assertEqual(result, [])
  
  def test_no_links_and_non_splittable(self):
      node = TextNode("Hello world", TextType.TEXT)
      node2 = TextNode("code", TextType.CODE)
      result = split_nodes_links([node, node2])
      self.assertEqual(result, [node, node2])
  
  def test_single_link(self):
      node = TextNode("Hello [text](url) world", TextType.TEXT)
      result = split_nodes_links([node])
      expected = [
          TextNode("Hello ", TextType.TEXT),
          TextNode("text", TextType.LINK, "url"),
          TextNode(" world", TextType.TEXT)
      ]
      self.assertEqual(result, expected)

  def test_multiple_links(self):
      node = TextNode(
          "Start [text1](url1) middle [text2](url2) end", 
          TextType.TEXT
      )
      result = split_nodes_links([node])
      expected = [
          TextNode("Start ", TextType.TEXT),
          TextNode("text1", TextType.LINK, "url1"),
          TextNode(" middle ", TextType.TEXT),
          TextNode("text2", TextType.LINK, "url2"),
          TextNode(" end", TextType.TEXT)
      ]
      self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()