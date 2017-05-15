#!/usr/env/bin python
import unittest
from markdown import Parser
from markdown import CommonHTMLPrinter


class TestCommonHTMLPrinterSetext(unittest.TestCase):

    def test_common__0_27__52(self):
        code = 'Foo\n-------------------------\n\nFoo\n='
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<h2>Foo</h2>\n<h1>Foo</h1>\n', html)

    def test_common__0_27__53(self):
        code = '   Foo\n---\n\n  Foo\n-----\n\n  Foo\n  ==='
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<h2>Foo</h2>\n<h2>Foo</h2>\n<h1>Foo</h1>\n', html)

    def test_common__0_27__55(self):
        code = 'Foo\n   ----      '
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<h2>Foo</h2>\n', html)

    def test_common__0_27__56(self):
        code = 'Foo\n    ----      '
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<p>Foo\n----</p>\n', html)

    def test_common__0_27__57_a(self):
        code = 'Foo\n= ='
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<p>Foo\n= =</p>\n', html)

    def test_multi_line(self):
        code = 'a\nb\n==='
        paragraphs = Parser.parse(code)
        html = str(CommonHTMLPrinter(paragraphs))
        self.assertEqual('<h1>a\nb</h1>\n', html)