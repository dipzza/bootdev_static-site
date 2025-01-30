import unittest

from mardown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
  def test_base(self):
    text = (
      "# This is a heading\n\n"
      "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n"
      "* This is the first list item in a list block"
      "* This is a list item"
      "* This is another list item"
    )
    result = markdown_to_blocks(text)
    expected = [
      "# This is a heading",
      "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
      ("* This is the first list item in a list block"
      "* This is a list item"
      "* This is another list item")
    ]
    self.assertEqual(result[1], expected[1])
    self.assertEqual(result, expected)

  def test_too_many_newlines(self):
    text = (
      "# This is a heading\n\n\n"
      "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n"
      "* This is the first list item in a list block"
      "* This is a list item"
      "* This is another list item"
    )
    result = markdown_to_blocks(text)
    expected = expected = [
      "# This is a heading",
      "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
      ("* This is the first list item in a list block"
      "* This is a list item"
      "* This is another list item")
    ]
    self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()