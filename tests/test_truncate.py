from typing import Any

import pytest

from textutils import truncate


def test_normal_case() -> None:
    assert truncate("Hello World", 8) == "Hello..."


def test_short_text_unchanged() -> None:
    assert truncate("Hi", 5) == "Hi"
    assert truncate("Hello", 5) == "Hello"


def test_tiny_max_len() -> None:
    assert truncate("Hello World", 2) == ".."
    assert truncate("Hello World", 0) == ""


def test_empty_text() -> None:
    assert truncate("", 0) == ""
    assert truncate("", 5) == ""


def test_custom_suffix() -> None:
    assert truncate("Hello World", 7, suffix="~") == "Hello ~"
    assert truncate("Hello World", 5, suffix="") == "Hello"


def test_exact_length() -> None:
    assert len(truncate("x" * 1000, 10)) == 10


def test_negative_max_len() -> None:
    with pytest.raises(ValueError):
        truncate("abc", -1)


@pytest.mark.parametrize("bad", [None, 5, b"x", ["a"]])
def test_non_str_text(bad: Any) -> None:
    with pytest.raises(TypeError):
        truncate(bad, 3)


@pytest.mark.parametrize("bad", [None, "3", 2.5, True])
def test_non_int_max_len(bad: Any) -> None:
    with pytest.raises(TypeError):
        truncate("abc", bad)


def test_error_messages_do_not_leak_text() -> None:
    with pytest.raises(ValueError) as exc:
        truncate("secret-text", -1)
    assert "secret-text" not in str(exc.value)
    bad_len: Any = "x"
    with pytest.raises(TypeError) as exc2:
        truncate("secret-text", bad_len)
    assert "secret-text" not in str(exc2.value)
