class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                live = 0

                for r in range(max(0, i - 1), min(rows, i + 2)):
                    for c in range(max(0, j - 1), min(cols, j + 2)):
                        if (r, c) != (i, j) and board[r][c] in (1, 2):
                            live += 1

                if board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 2  # Alive -> Dead
                elif board[i][j] == 0:
                    if live == 3:
                        board[i][j] = -1  # Dead -> Alive

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1