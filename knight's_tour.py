import time

board = []
try:  # to eliminate wrong input
    n = int(input("Enter board size:"))
except ValueError:
    n = 8
    print("You entered an invalid parameter,set by default", n)


def PrintBoard(j, k):  # creates a chessboard matrix
    for i in range(j):
        row = []
        for i in range(k):
            row.append('■')
        board.append(row)
    for i in range(k):
        print(board[i], "\n")


PrintBoard(n, n)

try:  # to eliminate wrong input
    x = int(input('Enter x coordinate:'))
    y = int(input('Enter y coordinate:'))
    board[x][y] = '♞'
except  ValueError:
    x = 0
    y = 0
    board[x][y] = '♞'
    print("You entered wrong coordinates, they are set by default", x, "and", y)
except IndexError:
    x = 0
    y = 0
    board[x][y] = '♞'
    print("You entered wrong coordinates, they are set by default", x, "and", y)
start = time.time()  # start time is fixed
stepx = []  # x line step list
stepy = []  # y line step list
stepx.append(x)
stepy.append(y)
def Move_calculation(x, y):  # reads the right moves
    j = 1
    a = [1, 1, 2, 2, -1, -1, -2, -2]
    b = [2, -2, 1, -1, 2, -2, 1, -1]
    for i in range((n * n) - 1): # read steps
        maxsteps = 8
        for i in range(len(a)):  # read step
            newx = x + a[i]
            newy = y + b[i]
            c = False
            if newx < 0 or newy < 0 or newx > n - 1 or newy > n - 1:  # coordinates in non-matrixes are excluded
                continue
            for i in range(len(stepx)):  # check originality of coordinates
                if newx == stepx[i] and newy == stepy[i]:
                    c = True
            if c:
                continue
            else:
                listx = []  # list of possible steps along the line x
                listy = []  # list of possible steps along the line y
                for i in range(len(a)):  # possible continuation of the step is read
                    allx = newx + a[i]
                    ally = newy + b[i]
                    if allx < 0 or ally < 0 or allx > n - 1 or ally > n - 1:  # coordinates in non-matrixes are excluded
                        continue
                    c = False
                    for i in range(len(stepx)):  # check originality of coordinates
                        if allx == stepx[i] and ally == stepy[i]:
                            c = True
                    if c:
                        continue
                    else:
                        listx.append(allx)
                        listy.append(ally)
                if len(listx) <= maxsteps:  # a step is selected with the minimum possible continuation
                    maxsteps = len(listx)
                    truex = newx
                    truey = newy
        x = truex
        y = truey
        stepx.append(x)
        stepy.append(y)
        board[x][y] = j   # on the place of the step the number of the step is written
        j += 1


Move_calculation(x, y)
print('*********************************', "\n")
PrintBoard(n, n)
print('*********************************')
print(time.time() - start, 'Seconds')
if len(stepx) == n ** 2:  # compares the number of moves made and the squares on the board
    print("Task completed successfully")
else:
    print("Something went wrong")
