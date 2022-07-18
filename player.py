import math
import random

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # check that the user input is a correct value by trying to cast
            # it to an interger and if not then it's invalid and an error is raised
            # also if the spot is not available, its also invalid
            try:
                val = int(square) 
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful
            except ValueError:
                print('Invalid sqaure. Try again.')
        return val    
