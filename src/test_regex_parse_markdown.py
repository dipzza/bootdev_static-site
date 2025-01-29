import unittest

from regex_parse_markdown import extract_markdown_images, extract_markdown_links

class TestRegexParse(unittest.TestCase):
    def test_extract_image(self):
        markdown = "![alt text](https://example.com/image.png)"
        result = extract_markdown_images(markdown)
        expected = [("alt text", "https://example.com/image.png")]
        self.assertEqual(result, expected)

    def test_extract_images(self):
        markdown = "![first](https://img1.com) and ![second](https://img2.com)"
        result = extract_markdown_images(markdown)
        expected = [("first", "https://img1.com"), ("second", "https://img2.com")]
        self.assertEqual(result, expected)

    def test_extract_no_images(self):
        markdown = "No images here!"
        result = extract_markdown_images(markdown)
        self.assertEqual(result, [])

    def test_extract_link(self):
        markdown = "[Boot.dev](https://www.boot.dev)"
        result = extract_markdown_links(markdown)
        expected = [("Boot.dev", "https://www.boot.dev")]
        self.assertEqual(result, expected)

    def test_extract_link(self):
        markdown = "[Google](https://google.com) and [YouTube](https://youtube.com)"
        result = extract_markdown_links(markdown)
        expected = [("Google", "https://google.com"), ("YouTube", "https://youtube.com")]
        self.assertEqual(result, expected)

    def test_extract_link(self):
        markdown = "No links here!"
        result = extract_markdown_links(markdown)
        expected = []
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()