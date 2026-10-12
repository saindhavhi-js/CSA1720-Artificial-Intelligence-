def solve(board, row):
    if row == 8:
        print(board)
        return True

    for col in range(8):
        if all(board[i] != col and abs(board[i]-col) != row-i
               for i in range(row)):
            board[row] = col
            if solve(board, row+1):
                return True
    return False

board = [-1] * 8
solve(board, 0)
