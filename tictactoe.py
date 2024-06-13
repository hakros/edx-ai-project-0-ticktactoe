"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    player1_moves = 0
    player2_moves = 0

    xLen = len(board[0])
    yLen = len(board)

    boardArea = xLen * yLen

    for i in range(boardArea):
        yPos = i // yLen
        xPos = i % xLen

        if board[yPos][xPos] == X:
            player1_moves += 1
        elif board[yPos][xPos] == O:
            player2_moves += 1

    return O if player1_moves > player2_moves else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = []

    xLen = len(board[0])
    yLen = len(board)

    boardArea = xLen * yLen

    for i in range(boardArea):
        yPos = i // yLen
        xPos = i % xLen

        if board[yPos][xPos] != EMPTY:
            continue

        possibleActions.append((yPos, xPos))

    return possibleActions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
