from datetime import date
from typing import Optional


def hello(name: str) -> str:
    """Return a simple greeting: 'Hello {name}'."""

    return f"Hello {name}"


def hello_with_date(name: str, today: Optional[date] = None) -> str:
    """Return a greeting that includes the date.

    Format: 'Hello {name}, today is YYYY-MM-DD'.
    If `today` is not provided, uses the current local date.
    """

    if today is None:
        today = date.today()

    return f"Hello {name}, today is {today.isoformat()}"
