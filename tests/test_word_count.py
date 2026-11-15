from typing import Any

import pytest

from textutils import word_count


def test_normal_case() -> None:
    assert word_count("one two  three\nfour") == 4


def test_single_word() -> None:
    assert word_count("hello") == 1


def test_empty_string() -> None:
    assert word_count("") == 0


def test_whitespace_only() -> None:
    assert word_count("   ") == 0
    assert word_count(" \t\n ") == 0


@pytest.mark.parametrize("value", [None, 5, 1.5, b"a b", ["a"]])
def test_non_str_raises_type_error(value: Any) -> None:
    with pytest.raises(TypeError):
        word_count(value)


def test_type_error_message_has_no_input() -> None:
    value: Any = 123456789
    with pytest.raises(TypeError) as excinfo:
        word_count(value)
    assert "123456789" not in str(excinfo.value)


def test_large_input() -> None:
    assert word_count("ab " * 300_000) == 300_000
