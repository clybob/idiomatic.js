

class TokenType:
    SPACE = 1
    LINE_TERMINATOR = 2
    COMMENT_IN_LINE = 3
    OTHER = 300


TOKENS = [{
    'chars': [u'\u0020', '\t', u'\u000B', u'\u000C', u'\u00A0' u'\uFFFF'],
    'TokenType': TokenType.SPACE
},
{
    'chars': [u'\u000A', u'\u000D', u'\u2028', u'\u2029'],
    'TokenType': TokenType.LINE_TERMINATOR
},
{
    'chars': ['//'],
    'TokenType': TokenType.COMMENT_IN_LINE
}]


def generate_tokens(code):
    i = 0

    def test_big_token(token, i):
        size = len(token['chars'][0])
        if code[i:i + size] == token['chars'][0]:
            return token['TokenType']
        else:
            return TokenType.OTHER

    while i < len(code):
        char = code[i]

        for tt in TOKENS:
            yield test_big_token(tt, i)

        i += 1
