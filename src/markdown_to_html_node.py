from block_to_block_type import BlockType, block_to_block_type
from htmlnode import ParentNode
from mardown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import textnode_to_htmlnode

def count_starting_chars(text, char):
  count = 0
  for letter in text:
    if letter == char:
      count += 1
    else:
      break
  return count

def get_block_html_tag(block, block_type):
  match block_type:
    case BlockType.HEADING:
      return f"h{count_starting_chars(block, "#")}"
    case BlockType.CODE:
      return "code"
    case BlockType.QUOTE:
      return "blockquote"
    case BlockType.UNORDERED_LIST:
      return "ul"
    case BlockType.ORDERED_LIST:
      return "ol"
    case BlockType.PARAGRAPH:
      return "p"
    case _:
      raise Exception(f"Unsupported block type {block_type}")
    
def strip_markdown_from_block(block, block_type):
  
  match block_type:
    case BlockType.HEADING:
      return block.lstrip("#").strip()
    case BlockType.CODE:
      return block.strip("```").strip()
    case BlockType.QUOTE:
      return block.lstrip(">").strip()
    case BlockType.UNORDERED_LIST:
      lines = block.split("\n")
      return [line[2:] for line in lines]
    case BlockType.ORDERED_LIST:
      lines = block.split("\n")
      return [line[3:] for line in lines]
    case BlockType.PARAGRAPH:
      return block
    case _:
      raise Exception(f"Unsupported block type {block_type}")
    

def text_to_htmlnodes(text):
  textnodes = text_to_textnodes(text)
  return [textnode_to_htmlnode(text_node) for text_node in textnodes]

    
def markdown_to_html_node(markdown):
  blocks = markdown_to_blocks(markdown)
  children = []

  for block in blocks:
    block_type = block_to_block_type(block)
    tag = get_block_html_tag(block, block_type)
    stripped_markdown = strip_markdown_from_block(block, block_type)

    if block_type == BlockType.UNORDERED_LIST or block_type == BlockType.ORDERED_LIST:
      list_children = [ParentNode("li", text_to_htmlnodes(item_text)) for item_text in stripped_markdown]
      children.append(ParentNode(tag, list_children))
      continue
    
    block_children = text_to_htmlnodes(stripped_markdown)

    if block_type == BlockType.CODE:
      code_node = ParentNode(tag, block_children)
      children.append(ParentNode("pre", [code_node]))
      continue

    children.append(ParentNode(tag, block_children))

  return ParentNode("div", children)