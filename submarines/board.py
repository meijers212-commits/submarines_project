def create_matrix(size: int, fill: int = 0) -> list[list[int]]:
    return [[fill for i in range(size)]for i in range(size)]

def create_bool_matrix(size: int, fill: bool = False) -> list[list[bool]]:
    return [[fill for i in range(size)]for i in range(size)]

def in_bounds(size: int, x: int, y: int) -> bool:
     return x <= size >= y

def count_remaining_ships_cells(ships: list[list[int]], shots: list[list[bool]]) -> int:
    count = 0
    for i in range(len(ships)):
        for j in range(len(shots)):
            if ships[i][j] and not shots[i][j] :
                count += 1
    return count

def render_public(ships: list[list[int]], shots: list[list[bool]]) -> str:
    count = 1
    res = "[ A B C E F G H I J ] \n"
    for i in range(len(ships)):
        for j in range(len(ships)):
            if not shots[i][j]:
                res += "o "
            if shots[i][j] and ships[i][j] == 0:
                res += "x "
            if shots[i][j] and ships[i][j] == 1:
                res += "v "
        res += f"[{str(count)}] \n"
        count += 1
    return res

def render_reveal(ships: list[list[int]], shots: list[list[bool]]) -> str:
    count = 1
    res = "[ A B C E F J H I J ] \n"
    for i in range(len(ships)):
        for j in range(len(ships)):
            if not shots[i][j]:
                if ships[i][j]:
                    res += "1 "
                else:
                    res += "o "
            if shots[i][j] and ships[i][j] == 0:
                res += "x "
            if shots[i][j] and ships[i][j] == 1:
                res += "v "
        res += f"[{str(count)}] \n"
        count += 1
    return res

