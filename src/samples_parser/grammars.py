grm_contained_str = r"""
contained_string: "\"" CONT_STRING "\""
                  | "'" CONT_STRING "'"
                  | "(" CONT_STRING ")"
                  | "{" CONT_STRING "}"
                  | "[" CONT_STRING "]"
CONT_STRING: /[\w.,!?:\- ]+/
"""

grm_imports = r"""
%import common.LETTER
%import common.NUMBER
"""
