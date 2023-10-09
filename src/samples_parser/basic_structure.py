from collections import ChainMap
from lark import Discard, Lark, Transformer, Tree

samples_grammar = r"""
start: [_NL] sample_source+
sample_source: source_info usage
usage: usage_info+

source_info: order "." name points stats _NL
usage_info: samples "-" band_info [_NL]
samples: sample_info+

order: INT
name: SENTENCE
points: contained_string
stats: contained_string

sample_info: sample "*"* timestamps "*"* sample_note "*"* _NL
sample: contained_string
sample_note: contained_string?
timestamps: ("@" TIMESTAMP ("," TIMESTAMP)*)?
TIMESTAMP: INT ":" ["0"] INT

band_info: band ";" song ";" album _NL band_note?

band_note: contained_string _NL

contained_string: quoted | parenthesis | braces | brackets
quoted      : /([\"\'])(.*?)(\1)/s
parenthesis : "(" STR_PAREN ")"
braces      : "{" STR_BRACE "}"
brackets    : "[" STR_BRACK "]"

band:SENTENCE
song:SENTENCE
album:SENTENCE | contained_string

STR_PAREN: (STRING_NL | "[" | "]" | "{" | "}" | "\"" | "@" | "'" | "." | ";")+
STR_BRACE: (STRING_NL | "[" | "]" | "(" | ")" | "\"" | "@" | "'" | "." | ";")+
STR_BRACK: (STRING_NL | "(" | ")" | "{" | "}" | "\"" | "@" | "'" | "." | ";")+
STRING_NL: /[\w.,!?:\- \&=+*\n\"\/#<>°%]/
STRING: /[\w.,!?:\- \&\(\)=+*\"\/\'\^<>#$%@°]/
WORD: STRING+
SENTENCE: WORD [" " WORD]*

%import common.INT
%import common.LETTER
%ignore " "
%import common.CR
%import common.LF
_NL: CR? LF

"""


class SamplesTransformer(Transformer):
    def SENTENCE(self, node):
        return str(node).strip()

    def __default__(self, data, children, meta):
        return Tree(data, children, meta)

    def quoted(self, nodes):
        return nodes[0].strip("'").strip('"')

    def contained_string(self, nodes):
        if isinstance(nodes[0], str):
            return nodes[0]
        else:
            return nodes[0].children[0].value

    def sample_note(self, nodes):
        if nodes != []:
            note = nodes[0].replace('\n', '')
            import re

            note = re.sub(re.compile(r'  +'), ' ', note)
        else:
            note = None
        return {'sample_note': note}

    def timestamps(self, nodes):
        if len(nodes):
            return {'timestamps': str([node.value for node in nodes])}
        else:
            return {'timestamps': None}

    def sample(self, nodes):
        return {'sample': nodes[0]}

    def band(self, nodes):
        return {'band': nodes[0]}

    def song(self, nodes):
        return {'song': nodes[0]}

    def album(self, nodes):
        return {'album': nodes[0]}

    def band_note(self, nodes):
        return {'band_note': nodes[0]}

    def points(self, nodes):
        return {'points': int(nodes[0].split()[0])}

    def name(self, nodes):
        return {'name': nodes[0]}

    def order(self, nodes):
        return {'order': int(nodes[0])}

    def stats(self, nodes):
        return {stat.split()[1]: int(stat.split()[0]) for stat in nodes[0].split(', ')}

    def sample_info(self, nodes):
        sample_info = dict(ChainMap(*nodes))
        if (
            sample_info['sample_note'] is None
            and sample_info['timestamps'] is None
            and 'Note' in sample_info['sample']
        ):
            # print(f'Discarding: {sample_info}')
            # file.write(f'{str(sample_info["sample"])}\n')
            return Discard
        else:
            return sample_info

    def band_info(self, nodes):
        return dict(ChainMap(*nodes))

    def source_info(self, nodes):
        return dict(ChainMap(*nodes))

    def samples(self, nodes):
        return nodes

    def usage_info(self, nodes):
        for node in nodes[0]:
            node.update(nodes[1])
        return nodes[0]

    def usage(self, nodes):
        usage = []
        for node in nodes:
            usage.extend(node)
        return usage

    def sample_source(self, nodes):
        for node in nodes[1]:
            node.update(nodes[0])
        return nodes[1]

    def start(self, nodes):
        start = []
        for node in nodes:
            start.extend(node)
        return start

samples_parser = Lark(grammar=samples_grammar)
samples_transformer = SamplesTransformer()
