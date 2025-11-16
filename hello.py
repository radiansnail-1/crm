from datetime import date


def hello(name: str) -> str:
    return f"Hello {name}"


def hello_with_date(name: str) -> str:
    today = date.today().isoformat()
    return f"Hello {name}, today is {today}"
