from textnode import TextNode, TextType


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


    
