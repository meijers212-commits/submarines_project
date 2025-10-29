from submarines.game import shoot,init_game,is_won,is_lost
from submarines.io import print_end,print_status,parse_coords
from submarines.placement import place_random_ships

def play(size: int = 10, n_ships: int = 17, max_shots: int = 25) -> None:
    manage_game = init_game(size, n_ships, max_shots)
    place_random_ships(manage_game["ships"])
    while True:
        print_status(manage_game)
        coll_input = input("please choose a column Coordination : ")
        row_input = input("please choose a row Coordination : ")
        chck_coordination = parse_coords(row_input,coll_input)

        if chck_coordination:
            shoot(manage_game,chck_coordination[0],chck_coordination[1])
            print_end(manage_game,is_won(manage_game),is_lost(manage_game))
            if is_lost(manage_game) or is_lost(manage_game):
                break





if __name__=="__main__":
    play()


