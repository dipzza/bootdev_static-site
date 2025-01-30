import re
 
TITLE_REGEX = "# (.*)"
IMAGE_REGEX = "!\[(.*?)\]\((.*?)\)"
LINK_REGEX = "\[(.*?)\]\((.*?)\)"

def extract_title(text):
  match = re.search(TITLE_REGEX, text)
  if match:
      return match.group(1)
  raise Exception("No title")

def extract_markdown_images(text):
  return re.findall(IMAGE_REGEX, text)

def extract_markdown_links(text):
  return re.findall(LINK_REGEX, text)