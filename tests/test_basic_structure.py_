import sys
import pytest
from rich import print as rprint

from samples_parser.basic_structure import (
    basic_structure_parser,
    basic_structure_transformer,
)

basic_text = """
1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
  "Move on, move on." (Note: Police robot addressing crowd gathering after
   a shootout)
    - Age of Chance; This is Crush Collision; One Thousand Years of Trouble
"""

basic_tranformed = [
  {
    'source_rank': 1,
    'source_name': 'Blade Runner',
    'source_points': 738,
    'source_usage_groups': 87,
    'source_usage_songs': 116,
    'source_usage_samples': 221,
    'sample_text': 'Move on, move on.',
    'sample_note': 'Note: Police robot addressing crowd gathering after a shootout',
    'band': 'Age of Chance',
    'album': 'This is Crush Collision',
    'song': 'One Thousand Years of Trouble'
  }
]

@pytest.mark.parametrize(
  "text, expected",
  [
    pytest.param(basic_text, basic_tranformed, id='Basic sample type')
  ]
)
def test_basic_structure(text, expected):
  parsed = basic_structure_parser.parse(text)
  transformed = basic_structure_transformer.transform(parsed)
  with open('output.txt', 'w') as f:
    original_stdout = sys.stdout
    sys.stdout = f
    rprint(transformed)
    sys.stdout = original_stdout

  assert transformed == expected

