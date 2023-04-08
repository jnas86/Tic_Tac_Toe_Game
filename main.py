# dictinary to hold tiles of in row-col forlat based on letters shown on the board
dict_gameboard = {
    "AA": " ",
    "AB": " ",
    "AC": " ",
    "BA": " ",
    "BB": " ",
    "BC": " ",
    "CA": " ",
    "CB": " ",
    "CC": " ",

}


# show the game board
def print_gameboard():
    print(f"   A   B   C\n"
          f"  ------------\n"
          f"A| {dict_gameboard['AA']} | {dict_gameboard['AB']} | {dict_gameboard['AC']} \n"
          f" |------------\n"
          f"B| {dict_gameboard['BA']} | {dict_gameboard['BB']} | {dict_gameboard['BC']} \n"
          f" |------------\n"
          f"C| {dict_gameboard['CA']} | {dict_gameboard['CB']} | {dict_gameboard['CC']} \n")


# scans the winner reqirements
def scan_for_winner():
    if dict_gameboard['AA'] == dict_gameboard['AB'] == dict_gameboard['AC'] and dict_gameboard['AB'] != " ":
        return True
    elif dict_gameboard['BA'] == dict_gameboard['BB'] == dict_gameboard['BC'] and dict_gameboard['BC'] != " ":
        return True
    elif dict_gameboard['CA'] == dict_gameboard['CB'] == dict_gameboard['CC'] and dict_gameboard['CC'] != " ":
        return True
    elif dict_gameboard['AA'] == dict_gameboard['BA'] == dict_gameboard['CA'] and dict_gameboard['CA'] != " ":
        return True
    elif dict_gameboard['AB'] == dict_gameboard['BB'] == dict_gameboard['CB'] and dict_gameboard['CB'] != " ":
        return True
    elif dict_gameboard['AC'] == dict_gameboard['BC'] == dict_gameboard['CC'] and dict_gameboard['CC'] != " ":
        return True
    elif dict_gameboard['AA'] == dict_gameboard['BB'] == dict_gameboard['CC'] and dict_gameboard['CC'] != " ":
        return True
    elif dict_gameboard['AC'] == dict_gameboard['BB'] == dict_gameboard['CA'] and dict_gameboard['CA'] != " ":
        return True
    else:
        return False


# game initiation
print("Welcome to Tic-Tac-Toe game")
print("Rules of the game: X plays first O second")
print("To make a move the player must give the row letter followed by the column letter e.g: AB ,23")
player_1 = input("Set name for Player 1: ")
player_2 = input("Set name for Player 2: ")

# sets X,O symbols to players
dict_symbols = {
    player_1: "X",
    player_2: "O"
}
print_gameboard()
game_is_finished = False
winner = ""
game_is_draw = True
current_player = player_1
# game loop
while game_is_finished is False:
    choice = input(f"{current_player} make choice: ").upper()
    try:
        if choice not in dict_gameboard:
            raise Exception("Invalid row/column letter choice")
        else:
            if dict_gameboard[choice] != " ":
                raise Exception("Cell is not empty.Choose an empty cell to play")
            else:
                dict_gameboard[choice] = f"{dict_symbols[current_player]}"
                print_gameboard()
                game_is_finished = scan_for_winner()
                if " " not in dict_gameboard.values() and scan_for_winner() is False:
                    game_is_finished = True
                if game_is_finished:
                    winner = current_player
                    game_is_draw = False
                if current_player == player_1:
                    current_player = player_2
                else:
                    current_player = player_1
    except Exception as e:
        print("Error: ", e)
if game_is_draw:
    print("There is no winner")
else:
    print(f"{winner} is the WINNER!!!")
