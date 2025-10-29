def init_game(size: int, n_ships: int, max_shots: int, *, rng: random.Random | None = None) -> dict:
     return {
      "size": int,
      "ships": list[list[int]],
      "shots": list[list[bool]],
      "n_ships": int,
      "max_shots": int,
      "shots_used": int
    }

def shoot(state: dict, x: int, y: int) -> tuple[bool, str]:
 # מבצע ירי אם לא נורה קודם ועל הגבולות; מחזיר (is_hit, message).
 # מעדכן shots_used רק בניסיון ירי תקין (לא ירי כפול/מחוץ לגבול).

def is_won(state: dict) -> bool:
 # כל תאי ה־1 נורו.

def is_lost(state: dict) -> bool:
 # shots_used >= max_shots ועדיין יש תאי צוללת לא־פגועים.

def shots_left(state: dict) -> int:

def remaining_ships(state: dict) -> int:

