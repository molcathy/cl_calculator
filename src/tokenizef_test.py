import pytest
import tokenizef


def test_get_tokens():
    assert tokenizef.get_tokens("5x^3 + 4x^2 - 4x - 4") == [
        "+5x^3",
        "+4x^2",
        "-4x",
        "-4",
    ]


def test_get_tokens_start_with_plus():
    assert tokenizef.get_tokens("+ 5x^3 + 4x^2 - 4x - 4") == [
        "+5x^3",
        "+4x^2",
        "-4x",
        "-4",
    ]


def test_get_tokens_start_with_plus_no_space():
    assert tokenizef.get_tokens("+5x^3 + 4x^2 - 4x - 4") == [
        "+5x^3",
        "+4x^2",
        "-4x",
        "-4",
    ]


def test_get_tokens_start_with_minus():
    assert tokenizef.get_tokens("- 5x^3 + 4x^2 - 4x - 4") == [
        "-5x^3",
        "+4x^2",
        "-4x",
        "-4",
    ]


def test_get_tokens_start_with_minus_no_space():
    assert tokenizef.get_tokens("-5x^3 + 4x^2 - 4x - 4") == [
        "-5x^3",
        "+4x^2",
        "-4x",
        "-4",
    ]


def test_get_tokens_no_spaces():
    assert tokenizef.get_tokens("5x^3 +4x^2 -4x -4") == ["+5x^3", "+4x^2", "-4x", "-4"]
