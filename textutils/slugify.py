"""slugify: turn text into a URL-friendly slug."""

import re
import unicodedata

_NON_SLUG = re.compile(r"[^a-z0-9]+")
_TRANSLIT = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"})


def slugify(text: str) -> str:
    """Return a URL-friendly slug for ``text``.

    Raises:
        TypeError: if ``text`` is not a ``str``.
    """
    if not isinstance(text, str):
        raise TypeError(f"text must be str, got {type(text).__name__}")
    lowered = text.lower().translate(_TRANSLIT)
    decomposed = unicodedata.normalize("NFKD", lowered)
    stripped = "".join(c for c in decomposed if not unicodedata.combining(c))
    return _NON_SLUG.sub("-", stripped).strip("-")
