import re
from functools import reduce
from lark import Lark, Transformer
from samples_parser.grammars import grm_contained_str

grammar_basic = r"""
start: [_NL] source_block

source_block: source_info sample_info song_info

source_info: source_rank " " source_name source_points source_usage _NL
sample_info: " "+ sample_text " " sample_note _NL
song_info: " "+ "- " band "; " album "; " song

source_rank: INT "."
source_name: STRING+
source_points: "[" INT " points] "
source_usage: "(" source_usage_groups source_usage_songs source_usage_samples")"
sample_text: contained_string
sample_note: contained_string

source_usage_groups: INT " groups, "
source_usage_songs: INT " songs, "
source_usage_samples: INT " samples"

band: STRING
album: STRING
song: STRING

STRING: (LETTER | NUMBER | "," | "." | "-" | "!" | "?" | ":")+ _NL?

%import common.LETTER
%import common.NUMBER
%import common.INT
%import common.WS -> _WS
%import common.NEWLINE -> _NL

%ignore _WS
%ignore _NL
"""
grammar = grammar_basic + grm_contained_str

basic_structure_parser = Lark(grammar=grammar)

class BasicStructureTransformer(Transformer):
    def compress_space(self, string):
        return re.sub(r'\s+', ' ', string)

    def __default__(self, data, children, meta):
        if data in ['source_rank', 'source_points', 'source_usage_groups', 'source_usage_songs', 'source_usage_samples']:
            return {str(data): int(children[0])}
        elif data in ['source_name', 'band', 'album', 'song', 'sample_text', 'sample_note']:
            return {str(data): str(children[0])}
        elif data in ['source_usage', 'source_info', 'sample_info', 'song_info', 'source_block']:
            return reduce(lambda x, y: dict(x, **y), children)
        elif data == 'contained_string':
            return self.compress_space(children[0])
        elif data == 'start':
            return children
        return super().__default__(data, children, meta)
    
    pass

basic_structure_transformer = BasicStructureTransformer()