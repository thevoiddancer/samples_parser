from lark import Lark, Transformer

# Grammar for grabbing quoted (single and double) and bracketed (braced, paranthesised)
# strings. Works on string contained within "'([{. Handles well the appearance of 
# non-opening characters (bracket in parenthesis, for example), but not the repeat of
# opening characters (brackets in brackets).
# NOTE: Does not remove the opening-closing quotes

contained_string_grammar = r"""
start: contained_string

contained_string: quoted | parenthesis | braces | brackets

quoted      : /([\"\'])(.*)(\1)/
parenthesis : "(" STR_PAREN ")"
braces      : "{" STR_BRACE "}"
brackets    : "[" STR_BRACK "]"

STR_PAREN: (STRING | "[" | "]" | "{" | "}")+
STR_BRACE: (STRING | "[" | "]" | "(" | ")")+
STR_BRACK: (STRING | "(" | ")" | "{" | "}")+
STRING: /[\w.,!?:\- ]/

"""

contained_string_parser = Lark(grammar=contained_string_grammar)

class CSTransformer(Transformer):
    def __default__(self, data, children, meta):
        return children[0].value

    def quoted(self, nodes):
        return nodes[0].strip("'").strip('"')

    def contained_string(self, nodes):
        return nodes[0]

    def start(self, nodes):
        return nodes[0]


transformer = CSTransformer()