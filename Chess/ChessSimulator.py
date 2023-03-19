class Chessboard:
    def __init__(self):
        self.board = [
            [-2, -3, -4, -6, -7, -4, -3, -2],
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [2, 3, 4, 6, 7, 4, 3, 2],
        ]
        self.why_illegal = ''
        self.player = 1

    @staticmethod
    def translate(move: str) -> (int, int, int, int):
        dic = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        f1 = dic[move[0]]
        f2 = 8 - int(move[1])
        t1 = dic[move[2]]
        t2 = 8 - int(move[3])
        return f2, f1, t1, t2

    def get_board(self):
        return self.board

    def make_move(self, move: str):
        if self.is_legal(move):
            if self.is_special(move):
                pass
            else:
                f1, f2, t1, t2 = self.translate(move)
                self.board[t1][t2] = self.board[f1][f2]
                self.board[f1][f2] = 0

        else:
            pass # nielegalny ruch

    def finished(self):
        return False

    def is_legal(self, move: str) -> bool:
        is_legal = True
        self.why_illegal = ''
        if self.is_special(move):
            return True
        else:
            f1, f2, t1, t2 = self.translate(move)
            if self.board[f1][f2] == 0: #sprawdzanie czy nie jest przesuwane puste pole
                is_legal = False
                self.why_illegal = self.why_illegal + 'Musisz przesunąć bierkę'
            if self.board[f1][f2]*self.player < 0:
                is_legal = False
                self.why_illegal = self.why_illegal + 'Musisz przesunąć własną bierkę'
        return is_legal

    def is_special(self, move):
        return False


def main():
    chessboard = Chessboard()

    while not chessboard.finished():
        move = input()
        chessboard.make_move(move)
        board = chessboard.get_board()
        print(board)


if __name__ == '__main__':
    main()
