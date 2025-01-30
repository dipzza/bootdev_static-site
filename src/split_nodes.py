from markdown_parsers import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes(old_nodes, extractor, extracted_to_markdown, text_type):
  new_nodes = []

  for old_node in old_nodes:
    matches = extractor(old_node.text)

    if len(matches) == 0 or old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    unprocessed_text = old_node.text
    for match in matches:
      sections = unprocessed_text.split(extracted_to_markdown(*match), 1)
    
      if len(sections[0]) > 0:
        new_nodes.append(TextNode(sections[0], TextType.TEXT))
      new_nodes.append(TextNode(match[0], text_type, match[1]))
      unprocessed_text = sections[-1]

    if len(unprocessed_text) > 0:
      new_nodes.append(TextNode(unprocessed_text, TextType.TEXT))
  
  return new_nodes

def build_markdown_image(alt_text, link):
  return f"![{alt_text}]({link})"

def build_markdown_link(text, url):
  return f"[{text}]({url})"

def split_nodes_images(old_nodes):
  return split_nodes(old_nodes, extract_markdown_images, build_markdown_image, TextType.IMAGE)

def split_nodes_links(old_nodes):
  return split_nodes(old_nodes, extract_markdown_links, build_markdown_link, TextType.LINK)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []

  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue

    sections = old_node.text.split(delimiter)

    if len(sections) % 2 == 0:
      raise Exception(f'Delimiter "{delimiter}" mismatch on "{old_node.text}"')
    
    for i in range(len(sections)):
      if len(sections[i]) == 0:
        continue
      if i % 2 == 0:
        new_nodes.append(TextNode(sections[i], TextType.TEXT))
      else:
        new_nodes.append(TextNode(sections[i], text_type))
  
  return new_nodes


    
