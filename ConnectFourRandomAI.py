import random

def AIcheck(game, token):  # randomly select a column
    available_moves = game.board.not_full_columns()
    return random.choice(available_moves)
