from enum import Enum

class BlockType(Enum):
  HEADING = "heading"
  CODE = "code"
  QUOTE = "quote"
  UNORDERED_LIST = "unordered_list"
  ORDERED_LIST = "ordered_list"
  PARAGRAPH = "paragraph"

def block_to_block_type(markdown):
  if markdown.startswith("#"):
      return BlockType.HEADING
  if markdown.startswith("```") and markdown.endswith("```"):
      return BlockType.CODE
  
  lines = markdown.split("\n")
  if all(line.startswith(">") for line in lines):
      return BlockType.QUOTE
  if all(line.startswith("* ") or line.startswith("- ") for line in lines):
      return BlockType.UNORDERED_LIST
  
  is_ordered_list = True
  for i in range(len(lines)):
      if not lines[i].startswith(f"{i+1}. "):
          is_ordered_list = False
          break

  if is_ordered_list:
      return BlockType.ORDERED_LIST
  
  return BlockType.PARAGRAPH
