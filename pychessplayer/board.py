class Board:
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]

    def printBoard(self):
        for row in self.board:
            for element in row:
                print(element, end=' ')
            print()  # Move to the next line after each row

    