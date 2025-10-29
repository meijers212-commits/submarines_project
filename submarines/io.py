from submarines.board import render_public,render_reveal
from submarines.game import remaining_ships,shots_left

def parse_coords(raw: str, column: str) -> tuple[int, int] | None:
    column = column.lower()
    alfa = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

    if column.isalpha() and column in alfa:
        column = alfa.index(column)
    else:
        return None

    if raw.isdigit():
        raw = int(raw) -1
    else:
        return None
    return raw, column

def print_status(state: dict) -> None:
    print(f'{render_public(state["ships"], state["shots"])} \n'
          f'you ave {state["max_shots"] - state["shots_used"]} attempts left \n '
          f'the ar {remaining_ships(state)} more ships compartments left')

def print_end(state: dict, won: bool, lost: bool) -> None:
    if won:
        print("you won! :).")
        print(render_reveal(state["ships"], state["shots"]))
    if lost:
        print("you loss! :-(.")
        print(render_reveal(state["ships"], state["shots"]))
    return



