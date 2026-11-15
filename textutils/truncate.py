"""truncate: shorten text to a maximum length."""


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Return ``text`` shortened to at most ``max_len`` characters.

    Text longer than ``max_len`` is cut so the result, including ``suffix``,
    is exactly ``max_len`` characters. If ``max_len`` is smaller than the
    suffix, the suffix itself is cut to ``max_len`` characters.

    Raises:
        TypeError: if ``text`` or ``suffix`` is not a ``str`` or ``max_len``
            is not an ``int`` (``bool`` is rejected).
        ValueError: if ``max_len`` is negative.
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    if not isinstance(max_len, int) or isinstance(max_len, bool):
        raise TypeError(f"max_len must be int, got {type(max_len).__name__}")
    if not isinstance(suffix, str):
        raise TypeError(f"suffix must be str, got {type(suffix).__name__}")
    if max_len < 0:
        raise ValueError("max_len must be >= 0")
    if len(text) <= max_len:
        return text
    if max_len < len(suffix):
        return suffix[:max_len]
    return text[: max_len - len(suffix)] + suffix
