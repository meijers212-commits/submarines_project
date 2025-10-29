import random
from submarines.board import *
def init_game(size: int, n_ships: int, max_shots: int, *, rng: random.Random | None = None) -> dict:
     return {
      "size": size,
      "ships": create_matrix(size),
      "shots": create_bool_matrix(size),
      "n_ships": n_ships,
      "max_shots": max_shots,
      "shots_used": 0
    }

def shoot(state: dict, raw: int, coll: int):
    if in_bounds(state["size"], raw, coll):
        if state["shots"][raw][coll]:
            print("this place as been already shot :| try agen.")
        else:
            state["shots_used"] += 1
            state["shots"][raw][coll] = True
            if state["ships"][raw][coll]:
                state["n_ships"] -= 1
                print("good thot! :).")
            else:
                print("bad thot! :(.")
    else:
        print("your shot is aut of bounds :{ .")
    return




def is_won(state: dict) -> bool:
    return not state["n_ships"] and shots_left(state)


def is_lost(state: dict) -> bool:
    return  state["n_ships"] and not shots_left(state)

def shots_left(state: dict) -> int:
    return state["max_shots"] - state["shots_used"]

def remaining_ships(state: dict) -> int:
    return state["n_ships"]


