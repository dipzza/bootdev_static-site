def markdown_to_blocks(markdown):
  blocks = markdown.split("\n\n")
  stripped = map(lambda x: x.strip(), blocks)
  return list(filter(lambda x: len(x) > 0, stripped))