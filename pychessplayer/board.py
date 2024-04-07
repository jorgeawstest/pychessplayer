import pieces

class Board:
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        for element in range(8):
            self.board[1][element] = pieces.Pawn()
            self.board[6][element] = pieces.Pawn()
        self.board[0][0] = pieces.Rook()
        self.board[0][7] = pieces.Rook()
        self.board[7][0] = pieces.Rook()
        self.board[7][7] = pieces.Rook()
        self.board[0][1] = pieces.Knight()
        self.board[0][6] = pieces.Knight()
        self.board[7][1] = pieces.Knight()
        self.board[7][6] = pieces.Knight()
        self.board[0][2] = pieces.Bishop()
        self.board[0][5] = pieces.Bishop()
        self.board[7][2] = pieces.Bishop()
        self.board[7][5] = pieces.Bishop()    
        self.board[0][3] = pieces.Queen()
        self.board[7][3] = pieces.Queen()
        self.board[0][4] = pieces.King()
        self.board[7][4] = pieces.King()
        

    def printBoard(self):
        for row in self.board:
            for element in row:
                print(element, end=' ')
            print()  # Move to the next line after each row
        

    