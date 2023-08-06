import pytest
from lark_samples.contained_string import contained_string_lark

@pytest.mark.parametrize(
    'string, expected',
    [
        pytest.params('"some text 123,.-!?"', 'some text 123,.-!?', id='double quotes'),
        pytest.params('\'some text 123,.-!?\'', 'some text 123,.-!?', id='single quotes'),
        pytest.params('[some text 123,.-!?]', 'some text 123,.-!?', id='brackets'),
        pytest.params('{some text 123,.-!?}', 'some text 123,.-!?', id='braces'),
        pytest.params('(some text 123,.-!?)', 'some text 123,.-!?', id='parenthesis'),
    ]
)
def test_contained_string(string, expected):
    