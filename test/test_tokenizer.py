import unittest
import sys
from os.path import join, abspath, dirname

sys.path.insert(0, abspath(join(dirname(''))) + '/..' )

from tokenizer import TokenType, generate_tokens


class TestTokenizer(unittest.TestCase):
    def setUp(self):
        code_js_file = open('fixtures/syntax.js')
        self.code_js = unicode(code_js_file.read())
        code_js_file.close()

    def test_tokenize_space(self):
        self.assertIn(TokenType.SPACE, generate_tokens(self.code_js))

    def test_tokenize_line_terminator(self):
        self.assertIn(TokenType.LINE_TERMINATOR, generate_tokens(self.code_js))

    def test_tokenize_comment(self):
        self.assertIn(TokenType.COMMENT_IN_LINE, generate_tokens(self.code_js))


if __name__ == '__main__':
    unittest.main()
