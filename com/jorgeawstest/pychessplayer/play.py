import argparse

def player(movements:str):
    print("inside player")

 def get_board():
    return "aaa"   

if __name__ == "__main__":  # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("movements", type=str)
    args = parser.parse_args()
    player(args.movements)
