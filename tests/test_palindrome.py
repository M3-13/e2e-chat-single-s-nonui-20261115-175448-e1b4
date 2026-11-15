import pytest

from textutils.palindrome import is_palindrome


def test_panama_sentence() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome() -> None:
    assert is_palindrome("hello") is False


def test_empty() -> None:
    assert is_palindrome("") is True


def test_punctuation_only() -> None:
    assert is_palindrome("!?, ...") is True


@pytest.mark.parametrize("bad", [None, 5, b"abba", ["a"]])
def test_type_error(bad: object) -> None:
    with pytest.raises(TypeError):
        is_palindrome(bad)


def test_type_error_message_has_no_input() -> None:
    with pytest.raises(TypeError) as exc:
        is_palindrome(12345)
    assert "12345" not in str(exc.value)


def test_long_input() -> None:
    assert is_palindrome("ab" * 500_000 + "ba" * 500_000) is True
