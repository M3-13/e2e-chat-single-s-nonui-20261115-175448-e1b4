# textutils

`textutils` ist eine kleine, eigenständige Python-Bibliothek mit fünf unabhängigen String-Hilfsfunktionen: `slugify`, `truncate`, `word_count`, `is_palindrome` und `reverse_words`. Alle Funktionen sind reine Funktionen: Sie lesen keine Dateien, Umgebungsvariablen oder Netzwerkressourcen, schreiben nichts in Logs und geben nichts aus. Es gibt keine Oberfläche und keinen Datenspeicher.

## Tech-Stack

- Python 3.11 oder neuer
- Packaging über `pyproject.toml` (setuptools)
- Keine Laufzeit-Abhängigkeiten, nur die Standardbibliothek
- Entwicklung: `pytest` (Tests) und `ruff` (Lint)

## Installation

```bash
pip install .
```

Für die Entwicklung (inklusive `pytest` und `ruff`):

```bash
pip install -e ".[dev]"
```

Danach lassen sich alle Funktionen importieren:

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```

## Verwendung

### `slugify(text: str) -> str`

Wandelt Text in einen URL-freundlichen Slug um.

```python
slugify("Hello, World!")  # 'hello-world'
```

### `truncate(text: str, max_len: int, suffix: str = "...") -> str`

Kürzt Text auf höchstens `max_len` Zeichen und hängt dabei `suffix` an.

```python
truncate("Hello World", 8)  # 'Hello...'
```

### `word_count(text: str) -> int`

Zählt die durch Leerraum getrennten Wörter.

```python
word_count("one two  three\nfour")  # 4
```

### `is_palindrome(text: str) -> bool`

Prüft, ob ein Text vorwärts und rückwärts gleich gelesen wird.

```python
is_palindrome("A man, a plan, a canal: Panama")  # True
```

### `reverse_words(text: str) -> str`

Kehrt die Reihenfolge der Wörter um.

```python
reverse_words("one two three")  # 'three two one'
```

## Fehlerverhalten

- Wird anstelle eines Strings ein anderer Typ als `text` übergeben (z. B. `None` oder `5`), lösen die Funktionen einen `TypeError` aus. Bei `truncate` gilt das auch für ein `max_len`, das kein `int` ist.
- `truncate` löst einen `ValueError` aus, wenn `max_len < 0` ist.
- Die Fehlermeldungen enthalten höchstens einen Typ- oder Parameternamen, nie den Eingabetext.

## Tests und Lint

```bash
pytest
ruff check .
ruff format --check .
```

## Funktionen

- `slugify`: URL-freundliche Slugs
- `truncate`: Text auf eine Maximallänge kürzen
- `word_count`: Wörter zählen
- `is_palindrome`: Palindrom-Prüfung
- `reverse_words`: Wortreihenfolge umkehren
