"""is_palindrome: check whether text reads the same in both directions."""


def is_palindrome(text: str) -> bool:
    """Return whether ``text`` is a palindrome.

    Only alphanumeric characters count and case is ignored. Text without any
    alphanumeric character is a palindrome.

    Raises:
        TypeError: if ``text`` is not a ``str``.
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    cleaned = [c.casefold() for c in text if c.isalnum()]
    return cleaned == cleaned[::-1]
