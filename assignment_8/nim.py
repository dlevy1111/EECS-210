# main program for creating the game board
from solution_search import decide

# main game board class
class Board(object):
    def __init__(self, board):
        self.board = board

    def update(self, piles, num):
        self.board[piles] -= num

    def computerUpdate(self, print_tree):
        self.board = decide(self.board, -float('inf'), float('inf'), True, print_tree)[1][1]

# check whether user input is valid
def isValid(remove, board):
    if not remove or len(remove) != 2: return False
    if remove[0] > 0 and remove[1] >= 0 and remove[1] < len(board) and remove[0] <= board[remove[1]]:
        return True
    return False
