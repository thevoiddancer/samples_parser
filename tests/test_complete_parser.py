import sys
import pytest
from rich import print as rprint

from samples_parser.basic_structure import (
    basic_structure_parser,
    basic_structure_transformer,
)

basic_text = """
1. Source 1 [738 points] (87 groups, 116 songs, 221 samples)
  "sample one, quote" @ 1:01 (Note: After sample)
  "sample two, quote"
  (Note: After all samples)
    - Band; Song; Album
    (Note: After the band)

  [sample one, sounds]
    - Band2; Song2; Album2

2. Source two [738 points] (87 groups, 116 songs, 221 samples)
  "sample one, quote"
    - Band; Song; Album
"""

basic_tranformed = [
  {
    'order': 1,
    'name': 'Source 1',
    'points': 738,
    'groups': 87,
    'songs': 116,
    'samples': 221,
    'sample': 'sample one, quote',
    'timestamps': "['1:01']",
    'sample_note': 'Note: After sample',
    'band': 'Band',
    'album': 'Album',
    'song': 'Song',
    'band_note': 'Note: After the band',
  },
  {
    'order': 1,
    'name': 'Source 1',
    'points': 738,
    'groups': 87,
    'songs': 116,
    'samples': 221,
    'sample': 'sample two, quote',
    'timestamps': None,
    'sample_note': None,
    'band': 'Band',
    'album': 'Album',
    'song': 'Song',
    'band_note': 'Note: After the band',
  },
  {
    'order': 1,
    'name': 'Source 1',
    'points': 738,
    'groups': 87,
    'songs': 116,
    'samples': 221,
    'sample': 'sample one, sounds',
    'timestamps': None,
    'sample_note': None,
    'band': 'Band2',
    'album': 'Album2',
    'song': 'Song2',
  },
  {
    'order': 2,
    'name': 'Source two',
    'points': 738,
    'groups': 87,
    'songs': 116,
    'samples': 221,
    'sample': 'sample one, quote',
    'timestamps': None,
    'sample_note': None,
    'band': 'Band',
    'album': 'Album',
    'song': 'Song',
  },
]

@pytest.mark.parametrize(
  "text, expected",
  [
    pytest.param(basic_text, basic_tranformed, id='Basic sample type')
  ]
)
def test_complete_parser(text, expected):
  parsed = basic_structure_parser.parse(text)
  transformed = basic_structure_transformer.transform(parsed)

  assert transformed == expected

