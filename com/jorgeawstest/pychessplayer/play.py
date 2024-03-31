import argparse
from pieces.pieces import King, Queen, Knight, Rook, Bishop, Pawn

def player(movements:str):
    print("inside player")
    king = King()
    king.move()
    queen = Queen()
    queen.move()
    rook = Rook()
    rook.move()
    knight = Knight()
    knight.move()
    bishop = Bishop()
    bishop.move()
    pawn = Pawn()
    pawn.move()

def get_board():
    return "aaa"   

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("movements", type=str)
    args = parser.parse_args()
    player(args.movements)
