import re
 
IMAGE_REGEX = "!\[(.*?)\]\((.*?)\)"
LINK_REGEX = "\[(.*?)\]\((.*?)\)"

def extract_markdown_images(text):
  return re.findall(IMAGE_REGEX, text)

def extract_markdown_links(text):
  return re.findall(LINK_REGEX, text)