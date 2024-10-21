class Solution:
    def get_box_id(self, row, col):
        row_val = (row // 3) * 3
        col_val = col // 3
        return row_val + col_val

    def is_valid(self, box, row, col, num):
        return str(num) not in box and str(num) not in row and str(num) not in col

    def solve_backtrack(self, board, boxes, rows, cols, r, c):
        if r == len(board) or c == len(board[0]):
            return True
        if board[r][c] == '.':
            for num in range(1, 10):
                num_val = str(num)
                board[r][c] = num_val
                box_id = self.get_box_id(r, c)
                box = boxes[box_id]
                row = rows[r]
                col = cols[c]
                if self.is_valid(box, row, col, num_val):
                    box[num_val] = True
                    row[num_val] = True
                    col[num_val] = True
                    if c == len(board[0]) - 1:
                        if self.solve_backtrack(board, boxes, rows, cols, r + 1, 0):
                            return True
                    else:
                        if self.solve_backtrack(board, boxes, rows, cols, r, c + 1):
                            return True
                    del box[num_val]
                    del row[num_val]
                    del col[num_val]
                board[r][c] = '.'
        else:
            if c == len(board[0]) - 1:
                if self.solve_backtrack(board, boxes, rows, cols, r + 1, 0):
                    return True
            else:
                if self.solve_backtrack(board, boxes, rows, cols, r, c + 1):
                    return True
        return False

    def solveSudoku(self, board):
        n = len(board)
        boxes = [{} for _ in range(n)]
        rows = [{} for _ in range(n)]
        cols = [{} for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if board[r][c] != '.':
                    box_id = self.get_box_id(r, c)
                    val = board[r][c]
                    boxes[box_id][val] = True
                    rows[r][val] = True
                    cols[c][val] = True
        self.solve_backtrack(board, boxes, rows, cols, 0, 0)

board = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
]
sol = Solution()
sol.solveSudoku(board)
for i in board:
    print(i)
