from lark import Lark
from rich import print as rprint
from samples_parser.grammars import grm_imports, grm_contained_str, grm_terminals

# Grammar for grabbing quoted (single and double) and bracketed (braced, paranthesised) strings
# Works on string contained within "'([{. Does not handle those characters inside the string.
# E.g. fails on "this is (parenthesis)"

grammar_start = r"""
start: contained_string"""

grammar = grammar_start + grm_contained_str + grm_terminals + grm_imports

contained_string_parser = Lark(grammar=grammar)
