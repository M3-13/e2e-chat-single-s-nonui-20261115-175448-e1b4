"""word_count: count the whitespace-separated words in a text."""


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``.

    Raises:
        TypeError: if ``text`` is not a ``str``.
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    return len(text.split())
