# btw this example which i am taking is considered to be the world'es toguhest sudoku problem.
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

# this function basically checks whether placing number n on the ith row and jth column is legal or not!
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
# this function gives the next vacant cell
def get_vacant():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i,j)
    return None
# this is a recursive function based on the idea of baktracking. 
def solver():
    next = get_vacant()
    if not next:
        return True
    x,y = next
    for i in range(1,10):
        if checker(x,y,i):
            board[x][y] = i
            if solver():
                return True
            board[x][y] = 0
    return False            


solved = solver()
if not solved :
    print("wrong sudoku!")

# finally printing the answer
for i  in range(9):
    for j in range(9):
        print(board[i][j],end="")
    print("\n",end = "")