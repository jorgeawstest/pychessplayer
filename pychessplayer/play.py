import argparse
from pieces import King, Queen, Knight, Rook, Bishop, Pawn
from board import Board, WHITE, BLACK
def player(movements:str):
    print("inside player")
    print(f"movements: {movements}")
    board = Board()
    board.printBoard()
    board.play(movements,WHITE)
    board.printBoard()


def get_board():
    return "aaa"   

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("--movements", type=str)
    args = parser.parse_args()
    player(args.movements)
