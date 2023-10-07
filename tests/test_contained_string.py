from samples_parser.contained_string import (
    contained_string_parser as parser,
    CSTransformer,
)

import pytest

samples = [
    '"sample"',
    "'sa'mple'",
    """'samp"le'""",
    "[sample]",
    "(sample)",
    "{sample}",
    "[sa(mple]",
    "[sam(pl)e]",
]

expected = [
    '"sample"',
    "'sa'mple'",
    """'samp"le'""",
    "sample",
    "sample",
    "sample",
    "sa(mple",
    "sam(pl)e",
]


@pytest.mark.parametrize("text, expected", [(txt, exp) for txt, exp in zip(samples, expected)])
def test_contained_string(text, expected):
    parsed = parser.parse(text)
    string = parsed.children[0].children[0].children[0].value
    assert string == expected


expected_trans = [
    "sample",
    "sa'mple",
    'samp"le',
    "sample",
    "sample",
    "sample",
    "sa(mple",
    "sam(pl)e",
]


@pytest.mark.parametrize(
    "text, expected", [(txt, exp) for txt, exp in zip(samples, expected_trans)]
)
def test_contained_string_transformer(text, expected):
    transformer = CSTransformer()
    parsed = parser.parse(text)
    transformed = transformer.transform(parsed)
    assert transformed == expected
