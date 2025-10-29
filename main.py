from submarines.game import *
from submarines.io import *

def play(size: int = 10, n_ships: int = 17, max_shots: int = 25) -> None:
    maneg_game = init_game(size, n_ships, max_shots)
    while True:
        print_status(maneg_game)
        row_input = input("please choose a row Coordination")



# 1.	אתחול מצב; 2) כל עוד לא ניצחון/הפסד ויש יריות — קלט קואורדינטות, ירי, הודעה;

# 2.	בסיום — תוצאה וחשיפה אם צריך.

# if __name__ == "__main__":
 # לטעון פרמטרים קבועים; למתקדמים — argparse לקריאת size, n_ships, max_shots, ואופציונלית --seed.

