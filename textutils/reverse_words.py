"""reverse_words: reverse the order of the words in a text."""


def reverse_words(text: str) -> str:
    """Return ``text`` with its words in reverse order, joined by single spaces.

    Raises:
        TypeError: if ``text`` is not a ``str``.
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    return " ".join(reversed(text.split()))
