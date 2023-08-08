from lark import Lark
from samples_parser.grammars import grm_contained_str

grammar_basic = r"""
start: [_NL] source_block

source_block: source_info sanple_info song_info

source_info: source_rank " " source_name source_points source_usage _NL
sanple_info: " "+ contained_string " " contained_string _NL
song_info: band "; " album "; " song

source_rank: INT "."
source_name: STRING
source_points: "[" INT " points] "
source_usage: "(" source_usage_groups source_usage_songs source_usage_samples")"

source_usage_groups: INT " groups, "
source_usage_songs: INT " songs, "
source_usage_samples: INT " samples"

band: STRING
album: STRING
song: STRING

STRING: (LETTER | NUMBER | " " | "," | "." | "-" | "!" | "?" | ":" | _NL)+

%import common.LETTER
%import common.NUMBER
%import common.INT
%import common.NEWLINE -> _NL
"""
grammar = grammar_basic + grm_contained_str

basic_structure_parser = Lark(grammar=grammar)