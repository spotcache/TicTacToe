from time import sleep 
from os import system

def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):

            if print_game:
                print(f'{letter} makes a move to square {square}. 🤔')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f'{letter} wins! 🎉')
                    sleep(2)
                    system('cls')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        sleep(.8)

    if print_game:
        print('It\'s a tie! 😲')
        sleep(2)
        system('cls')