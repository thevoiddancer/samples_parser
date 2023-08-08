grm_contained_str = r"""
contained_string: "\"" STRING "\""
                  | "'" STRING "'"
                  | "(" STRING ")"
                  | "{" STRING "}"
                  | "[" STRING "]"

"""

grm_terminals = r"""
STRING: (LETTER | NUMBER | " " | "," | "." | "-" | "!" | "?" | ":" )+

"""

grm_imports = r"""
%import common.LETTER
%import common.NUMBER
"""
