import time

import pytest

from textutils import slugify


def test_normal():
    assert slugify("Hello, World!") == "hello-world"


def test_umlauts():
    assert slugify("  Über uns & Co.  ") == "ueber-uns-co"
    assert slugify("Straße Köln") == "strasse-koeln"


def test_accents():
    assert slugify("Café Crème") == "cafe-creme"


def test_empty_and_special():
    assert slugify("") == ""
    assert slugify("!!!") == ""


@pytest.mark.parametrize("bad", [None, 5, b"x", ["a"]])
def test_type_error(bad):
    with pytest.raises(TypeError) as exc:
        slugify(bad)
    assert "x" not in str(exc.value).replace("text", "").replace("str", "")


def test_large_input_fast():
    start = time.perf_counter()
    assert slugify("a! " * 350_000) == "-".join(["a"] * 350_000)
    assert time.perf_counter() - start < 5
