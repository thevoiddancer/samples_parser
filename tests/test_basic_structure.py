from samples_parser.basic_structure import basic_structure_parser

text = """
1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
  "Move on, move on." (Note: Police robot addressing crowd gathering after
   a shootout)
    - Age of Chance; This is Crush Collision; One Thousand Years of Trouble
"""

def test_basic_structure():
    basic_structure_parser.parse(text)