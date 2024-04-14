class Piece:
    def __init__(self, color):
        self.color = color
    def move(self):
        print(self.name + " moving. My value is " + str(self.value) + " and my initial is: " + self.initial)
    def __str__(self):
        return f"{self.initial}"
class King(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.name = "king"
        self.initial = 'K'
        self.value = 999

class Queen(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.name = "queen"
        self.initial = 'Q'
        self.value = 9

class Rook(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.name = "rook"
        self.initial = 'R'
        self.value = 5

class Bishop(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.name = "bishop"
        self.initial = 'B'
        self.value = 3

class Knight(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.name = "knight"
        self.initial = 'N'
        self.value = 3

class Pawn(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.name = "pawn"
        self.initial = 'P'
        self.value = 1
