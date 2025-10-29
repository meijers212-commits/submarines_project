from submarines.board import *

def parse_coords(raw: str, column: str) -> tuple[int, int] | None:
    raw = raw.lower()
    alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    if raw.isalpha() and raw in alfa:
        raw = alfa.index(raw)
    else:
        return None

    if column.isdigit():
        column = int(column) -1
    else:
        return None
    return raw, column

def print_status(state: dict) -> None:
    print(f'{render_public(state["ships"], state["shots"])} \n'
          f'you ave {state["max_shots"] - state["used_shots"]} left \n '
          f'')

def print_end(state: dict, won: bool, lost: bool) -> None:
    if won:
        print("you won! :).")
    if lost:
        print("you loss! :-(.")
    print(render_reveal(state["ships"], state["shots"]))
    return



