
class Board:
    def __init__(self, size, X, O, EMPTY):
        self.X = X
        self.Y = O
        self.size = size
        self.EMPTY = EMPTY
        self.board = self.create(size)

    def create(self, size):
        return [[self.EMPTY for x in range(size)] for i in range(size)]

    def __str__(self):
        return "\n".join(map(lambda x: " ".join(x), self.board))

    def check_rows(self, player: str) -> bool:
        for row in self.board:
            if row.count(player) == len(row):
                return True
        return False

    def check_coulombs(self, player):
        marks = 0
        for i, row in enumerate(self.board):
            for j in range(len(self.board)):
                marks += self.board[j][i] == player
            if marks == len(row):
                return True
        return False

    def check_win(self, player):
        return self.check_coulombs(player) or self.check_rows(player)

    def update_board(self, player: str, cords: tuple[int, int]):
        self.board[cords[0]][cords[1]] = player



new_board = Board(8, "X", "O", "*")

# print(new_board)
new_board.update_board("X", (4, 7))
print(new_board)
# print(new_board.board)