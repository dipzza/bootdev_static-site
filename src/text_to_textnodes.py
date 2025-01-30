from split_nodes import split_nodes_delimiter, split_nodes_images, split_nodes_links
from textnode import TextNode, TextType

def text_to_textnodes(text):
  base_node = TextNode(text, TextType.TEXT)
  with_code = split_nodes_delimiter([base_node], "`", TextType.CODE)
  with_bold = split_nodes_delimiter(with_code, "**", TextType.BOLD)
  with_italics = split_nodes_delimiter(with_bold, "*", TextType.ITALIC)
  with_images = split_nodes_images(with_italics)
  return split_nodes_links(with_images)
