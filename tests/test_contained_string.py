import pytest
from samples_parser.contained_string import contained_string_parser
from lark import UnexpectedCharacters


@pytest.mark.parametrize(
    "string, error, expected",
    [
        pytest.param(
            '"some text 123,.-!?"', None, "some text 123,.-!?", id="double quotes"
        ),
        pytest.param(
            "'some text 123,.-!?'", None, "some text 123,.-!?", id="single quotes"
        ),
        pytest.param("[some text 123,.-!?]", None, "some text 123,.-!?", id="brackets"),
        pytest.param("{some text 123,.-!?}", None, "some text 123,.-!?", id="braces"),
        pytest.param(
            "(some text 123,.-!?)", None, "some text 123,.-!?", id="parenthesis"
        ),
        pytest.param(
            "(some text 123,.-!?(", UnexpectedCharacters, None, id="two opening"
        ),
        pytest.param(
            "\"some text 123,.-!?'", UnexpectedCharacters, None, id="mismatched quote"
        ),
        pytest.param(
            "[some text 123,.-!?)", UnexpectedCharacters, None, id="mismatched brace"
        ),
        pytest.param(
            "(some [text 123,.-!?)", UnexpectedCharacters, None, id="brace inside"
        ),
    ],
)
def test_contained_string(string, error, expected):
    if not error:
        result = contained_string_parser.parse(string)
        assert result.children[0].children[0] == expected
    else:
        with pytest.raises(error):
            contained_string_parser.parse(string)
