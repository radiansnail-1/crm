from datetime import date

from hello import hello, hello_with_date


def test_hello_basic() -> None:
    assert hello("Alice") == "Hello Alice"


def test_hello_with_date_given_date() -> None:
    fixed_date = date(2025, 11, 16)

    result = hello_with_date("Alice", fixed_date)

    assert result == "Hello Alice, today is 2025-11-16"
