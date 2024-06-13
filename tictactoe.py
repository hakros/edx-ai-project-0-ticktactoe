"""
Tic Tac Toe Player
"""

import math
import copy

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

    # Calculate the number of squares on the xAxis and yAxis of the board
    xLen = len(board[0])
    yLen = len(board)

    # Calcualte how many squares in total the board has
    boardArea = xLen * yLen

    # Loop through boardArea
    # For every X that we find, we add that to the number of moves that player1 has made
    # For every O that we find, we add that to the number of moves that player 2 has made
    for i in range(boardArea):
        # Division without decimal to find where we are i the y-axis
        yPos = i // yLen

        # Use modulo operation to find the remainder after division
        # This is our position in the x axis
        xPos = i % xLen

        if board[yPos][xPos] == X:
            player1_moves += 1
        elif board[yPos][xPos] == O:
            player2_moves += 1

    # If player 1 has more moves than player 2, it is player 1s turn
    # Else it is player 2s turn
    return O if player1_moves > player2_moves else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    # Calculate the number of squares on the xAxis and yAxis of the board
    xLen = len(board[0])
    yLen = len(board)

    # Calcualte how many squares in total the board has
    boardArea = xLen * yLen

    # Loop through boardArea
    for i in range(boardArea):
        # Division without decimal to find where we are i the y-axis
        yPos = i // yLen

        # Use modulo operation to find the remainder after division
        # This is our position in the x axis
        xPos = i % xLen

        # If the square is not empty, this is not a possible move
        if board[yPos][xPos] != EMPTY:
            continue

        possibleActions.add((yPos, xPos))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # The player that made the move
    playerToMove = player(board)
    possibleMoves = actions(board)

    # Create a deep copy of the board to avoid modifying the original board
    newBoard = copy.deepcopy(board)

    # Check if the action or move is a valid move
    if action not in possibleMoves or newBoard[action[0]][action[1]] != EMPTY:
        raise Exception

    newBoard[action[0]][action[1]] = playerToMove

    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # A list of winning moves
    winningMoves = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
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


def recurseMin(state, depth):
    """A recursive function that finds the lowest number of move before a win"""
    # Stop recursion once the game is over
    if terminal(state) is True:
        return depth

    possibleActions = actions(state)

    # Since we are finding the min value, we set the initial value as high as possible
    value = math.inf

    for possibleAction in possibleActions:
        newBoard = result(
            state,
            possibleAction
        )

        # Find the maximum number of moves before a win if this move is used
        # Every recursion, we add 1 to the depth or number of moves made
        newValue = recurseMax(newBoard, depth+1)

        # Use the lowest number of move between value and newValue
        value = min(value, newValue)

    # Return the lowest number of move until win
    return value


def recurseMax(state, depth):
    """A recursive function that finds the highest number of move before a win"""
    # Stop recursion once the game is over
    if terminal(state) is True:
        return depth

    possibleActions = actions(state)

    # Since we are finding the min value, we set the initial value as low as possible
    value = -(math.inf)

    for possibleAction in possibleActions:
        newBoard = result(
            state,
            possibleAction
        )

        # Find the minimum number of moves before a win if this move is used
        # Every recursion, we add 1 to the depth or number of moves made
        newValue = recurseMin(newBoard, depth+1)

        # Use the highest number of move between value and newValue
        value = max(value, newValue)

    # Return the highest number of move until win
    return value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # No more possible moves to make
    if terminal(board) is True:
        return None

    playerToMove = player(board)
    possibleActions = actions(board)

    # Stores the best move to use
    moveToUse = ()

    # Stores the number of moves until win
    # O is the min player so we set initial value as low as possible for him
    # X is the max player so we set initial value as high as possible for him
    # max player is always the first to move
    value = -(math.inf) if playerToMove == O else math.inf

    for possibleAction in possibleActions:
        newBoard = result(
            board,
            possibleAction
        )

        if playerToMove == O:
            # Find the lowest number of move before we lose, if we use this move
            newValue = recurseMin(newBoard, 0)

            # If this move gives us the lower chance to lose compared to the move stored in moveToUse,
            # This is the new best move
            # Example: 5 > 4 moves. 5 moves before lose is better than 4 moves before lose
            if (newValue > value):
                value = newValue
                moveToUse = possibleAction
        elif playerToMove == X:
            # Find the highest number of moves before we win, if we use this move
            newValue = recurseMax(newBoard, 0)

            # If this move gives us the higher chance to win compared to the move stored in moveToUse,
            # This is the new best move
            # Example 4 < 5 moves. 4 moves before win is better than 5 moves before win
            if (newValue < value):
                value = newValue
                moveToUse = possibleAction

    return moveToUse