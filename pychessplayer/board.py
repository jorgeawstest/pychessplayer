import pieces
WHITE = "White"
BLACK = "Black"
class Board:
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        for element in range(8):
            self.board[1][element] = pieces.Pawn(WHITE)
            self.board[6][element] = pieces.Pawn(BLACK)
        self.board[0][0] = pieces.Rook(WHITE)
        self.board[0][7] = pieces.Rook(WHITE)
        self.board[7][0] = pieces.Rook(BLACK)
        self.board[7][7] = pieces.Rook(BLACK)
        self.board[0][1] = pieces.Knight(WHITE)
        self.board[0][6] = pieces.Knight(WHITE)
        self.board[7][1] = pieces.Knight(BLACK)
        self.board[7][6] = pieces.Knight(BLACK)
        self.board[0][2] = pieces.Bishop(WHITE)
        self.board[0][5] = pieces.Bishop(WHITE)
        self.board[7][2] = pieces.Bishop(BLACK)
        self.board[7][5] = pieces.Bishop(BLACK)    
        self.board[0][3] = pieces.Queen(WHITE)
        self.board[7][3] = pieces.Queen(BLACK)
        self.board[0][4] = pieces.King(WHITE)
        self.board[7][4] = pieces.King(BLACK)        
    
    def printBoard(self):
        for row in self.board:
            for element in row:
                print(element, end=' ')
            print()  # Move to the next line after each row
        
    def play(self,movement,side):
        print(f"Playing movement: {movement} for side {side}")
        origin = (6,4)
        destination = (4,4)
        print(f"move: {type(origin)}")
        print(f"board: {self.board[origin[0]][origin[1]]}")
        self.board[destination[0]][destination[1]] = self.board[origin[0]][origin[1]]
        self.board[origin[0]][origin[1]] = 0
    
    def sayhello(self):
        return "hello"