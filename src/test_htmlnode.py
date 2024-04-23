import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        test_props = {"href": "https://www.google.com", "target": "_blank"}
        test_string = ' href="https://www.google.com" target="_blank"'
        node = HtmlNode(props=test_props)
        self.assertEqual(test_string, node.props_to_html())

    def test_leaf_node_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph of text.")
        test_html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(test_html, node.to_html())

    def test_leaf_node_to_html_no_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        test_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(test_html, node.to_html())
        
    def test_parent_node_to_html(self):
        test_node = ParentNode("p",[ LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text"), LeafNode(None, "Normal text"),],)
        test_string = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(test_string, test_node.to_html())
    

if __name__ == "__main__":
    unittest.main()
    