#!/usr/bin/python3
"""Solves the N-queens puzzle"""

  import sys

  def is_safe(board, row, col, size):
    """
    Check if it's safe to place a queen at the given row and column on the board.
    """
    return all(
        board[i][col] == 0 and
        all(board[i][j] == 0 for j in range(col)) and
        all(board[i - k][j - k] == 0 for k in range(min(row, col) + 1))
        for i, j in zip(range(row, -1, -1), range(col, -1, -1))

  def solve_nqueens_recursive(board, col, size):
    """
    Recursively solve the N Queens problem for a given column.
    """
    if col >= size:
        for row in board:
            print(' '.join(str(cell) for cell in row))
        print()
        return
    
    for row in range(size):
        if is_safe(board, row, col, size):
            board[row][col] = 1
            solve_nqueens_recursive(board, col + 1, size)
            board[row][col] = 0

  try:
    board_size = int(sys.argv[1])
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
  except (ValueError, IndexError):
    print("Usage: nqueens N")
    sys.exit(1)

  chessboard = [[0] * board_size for _ in range(board_size)]
  solve_nqueens_recursive(chessboard, 0, board_size)

