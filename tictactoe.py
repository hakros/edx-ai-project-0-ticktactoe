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
    # The player that made the move
    playerToMove = player(board)

    board[action[0]][action[1]] = playerToMove

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # A list of winning moves
    winningMoves = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],

        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],

        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)],
    ]

    # Our winning conditions
    winningConditions = [
        f"{X}{X}{X}",
        f"{O}{O}{O}",
    ]

    # The winning player
    winningPlayer = EMPTY

    # We use this to store the player(s) that made this winning move
    # Assumption is there should only be one player per winning move
    # Only OOO or XXX is allowed
    moveset = ''

    # Find a player that has won by looping through each winning moves
    for winningMove in winningMoves:
        # Reset moveset per winning move
        moveset = ''

        for move in winningMove:
            # The player that made this move
            playerToMove = board[move[0]][move[1]]

            # No player has used this move
            # Move on the the next winning move set
            if (playerToMove == EMPTY):
                break

            moveset += playerToMove

        # If the moveset is one of our winning conditions,
        # we have a winner. Stop the loop
        if moveset in winningConditions:
            winningPlayer = playerToMove
            break

    return winningPlayer


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Checks if there no more possible moves
    noPossibleMoves = len(actions(board)) == 0

    # Checks if there is a winner
    hasWinner = winner(board) != None

    return noPossibleMoves or hasWinner


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    newWinner = winner(board)

    if (newWinner == None):
        return 0

    return -1 if newWinner == O else 1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
