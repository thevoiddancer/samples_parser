import pytest
from samples_parser.basic_structure import samples_parser, samples_transformer

samples_text = """
1. Blade Runner [738 points] (87 groups, 116 songs, 221 samples)
  "Move on, move on." @ 1:01 (Note: one sample note, 
  breaks line)
  (Note: all samples note)
    - Age of Chance; This is Crush Collision; One Thousand Years of Trouble
    (Note: band note)
"""

# All samples note and band note are discarded
expected = [
    {
        'sample_note': 'Note: one sample note, breaks line',
        'timestamps': "['1:01']",
        'sample': 'Move on, move on.',
        'album': 'One Thousand Years of Trouble',
        'song': 'This is Crush Collision',
        'band': 'Age of Chance',
        'groups': 87,
        'songs': 116,
        'samples': 221,
        'points': 738,
        'name': 'Blade Runner',
        'order': 1,
    },
]


@pytest.mark.parametrize(
    'text, expected', [pytest.param(samples_text, expected, id='default')]
)
def test_parser(text, expected):
    parsed = samples_parser.parse(text)
    transformed = samples_transformer.transform(parsed)
    assert transformed == expected
