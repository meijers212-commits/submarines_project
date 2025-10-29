def parse_coords(raw: str, column: str) -> tuple[int, int] | None:
    raw = raw.lower()
    alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    if raw.isalpha() and raw in alfa:
        raw = alfa.index(raw)
    else:
        return None

    if column.isdigit():
        column = int(column)
    else:
        return None
    return raw, column

def print_status(state: dict) -> None:
    for row in state

# def print_end(state: dict, won: bool) -> None:
#     if won
#
# alfa = ["a","b","c","d","e","f","g","h","i","j"]

