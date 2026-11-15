from typing import Any

import pytest

from textutils import reverse_words


def test_normal_case() -> None:
    assert reverse_words("one two three") == "three two one"


def test_extra_whitespace() -> None:
    assert reverse_words("  a   b ") == "b a"


def test_empty_and_whitespace_only() -> None:
    assert reverse_words("") == ""
    assert reverse_words("  \t ") == ""


def test_long_input() -> None:
    assert reverse_words("ab " * 300_000) == "ab " * 299_999 + "ab"


@pytest.mark.parametrize("value", [None, 5, b"a b", ["a"]])
def test_non_str_raises_type_error(value: Any) -> None:
    with pytest.raises(TypeError) as exc:
        reverse_words(value)
    assert "a b" not in str(exc.value)
