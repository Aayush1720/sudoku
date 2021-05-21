board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]

def checker(i , j, n):
    for k in range(0,9):
        if board[k][j] == n:
            return False
    for k in range(0,9):
        if board[i][k] == n:
            return False
    i//=3
    j//=3
    for k in range(3*i,3*i+3):
        for l in range(3*j,3*j+3):
            if board[k][l] == n:
                return False
    return True