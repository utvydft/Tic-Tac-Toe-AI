"""
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
    x = 0
    o = 0
    for i in range(0, 3):
        for j in range(0, 3):
            # if the number of X & O pieces are the same, then it X turn else is O turn
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1
    if x == o:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # create a list for all the possible move sets
    ACTIONS = []
    for i in range(0, 3):
        for j in range(0,3):
            if board[i][j] == EMPTY:
                # go throught the board to find empty space and aoeend the corrinadates as a tuple
                ACTIONS.append((i, j))
    return ACTIONS


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check if the move is vaild
    if action not in actions(board):
        raise Exception("invaild move")
    # copy the board
    c = copy.deepcopy(board)
    # put the player piece in board copy (action is a tuple)
    c[action[0]][action[1]] = player(board)
    return c


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[1][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[1][1] != EMPTY:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] and board[1][1] != EMPTY:
        return board[2][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_space = False
    # checking for empty space and hrozoinal and vecitcal
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                empty_space = True
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != None:
            return True
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != None:
            return True
    # checking for diagional
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != None: 
        return True
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1] != None:
        return True
    if empty_space == False:
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == None:
        return 0
    elif win == X:
        return 1
    else:
        return -1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def max_value(state, c):
        if terminal(state):
            return utility(state)
        v = -20000
        for action in actions(state):
            mini = mini_value(result(state, action), 0)
            if v < mini:
                v = mini
                act = action
        if c == 1:
            return act
        return v
    
    def mini_value(state, c):
        if terminal(state):
            return utility(state)
        v = 20000
        for action in actions(state):
            maxi = max_value(result(state, action), 0)
            if v > maxi:
                v = maxi
                act = action
                
        if c == 1:
            return act
        return v

    if player(board) == X:
        return max_value(board, 1)
    else:
        return mini_value(board, 1)
