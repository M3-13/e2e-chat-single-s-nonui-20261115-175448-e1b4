import textutils

NAMES = ["slugify", "truncate", "word_count", "is_palindrome", "reverse_words"]


def test_names_importable() -> None:
    for name in NAMES:
        assert callable(getattr(textutils, name))


def test_names_in_all() -> None:
    for name in NAMES:
        assert name in textutils.__all__
