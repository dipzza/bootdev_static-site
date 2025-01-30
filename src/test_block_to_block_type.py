import unittest

from block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)

    def test_quote(self):
        self.assertEqual(block_to_block_type("> Quote\n> More Quote"), BlockType.QUOTE)

    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("- Item 1\n* Item 2"), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First\n2. Second\n3. Third"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1. First\n3. Second\n4. Third"), BlockType.PARAGRAPH)

    def test_paragraph(self):
        self.assertEqual(block_to_block_type("This is a normal paragraph."), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
