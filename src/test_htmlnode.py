import unittest

from htmlnode import HtmlNode


class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        test_props = {"href": "https://www.google.com", "target": "_blank"}
        test_string = ' href="https://www.google.com" target="_blank"'
        node = HtmlNode(props=test_props)
        self.assertEqual(test_string, node.props_to_html())


if __name__ == "__main__":
    unittest.main()
    