""" Solving n Queen problem:
Placing n chess queens on an n×n chessboard so that no two queens threaten each other."""

from random import randint
import sys
try:
    n = 20
    if n <= 3:
        throw
except:
    print('Error:\nChess dimension must be greater than 3')
chess = []
for a in range(n):
    row = [2] * n
    chess.append(row)
mess = []
for a in range(n**2):
    mess.append([])

#fill function determines which squares are under attack by the queen placed on (i,j)th square, 
def fill(i, j):
    global chess, mess
    chess[i][j] = 'Q'
    for a in range(n-1):
        chess[i - a - 1][j] = '-'
        mess[(i - a - 1) * n + j].append(i * n + j + 1)
        chess[i][j - a - 1] = '-'
        if (i + 1) * n - a - 1 > i * n + j:
            mess[(i + 1) * n - a - 1].append(i * n + j + 1)
        else:
            mess[(i + 1) * n - a - 2].append(i * n + j + 1)
        if i - a - 1 >= 0 and j - a - 1 >= 0:
            chess[i - a - 1][j - a - 1] = '-'
            mess[(i - a - 1) * n + j - a - 1].append(i * n + j + 1)
        if i - a - 1 >= 0 and j + a + 1 <= (n-1):
            chess[i - a - 1][j + a + 1] = '-'
            mess[(i - a - 1) * n + j + a + 1].append(i * n + j + 1)
        if i + a + 1 <= (n-1) and j - a - 1 >= 0:
            chess[i + a + 1][j - a - 1] = '-'
            mess[(i + a + 1) * n + j - a - 1].append(i * n + j + 1)
        if i + a + 1 <= (n-1) and j + a + 1 <= (n-1):
            chess[i + a + 1][j + a + 1] = '-'
            mess[(i + a + 1) * n + j + a + 1].append(i * n + j + 1)

#when placing a queen on (i,j)th squre in previous step makes a situation that there is no posibility to place another queen, we must change it's place. unfill finction clears all squares that "fill function" has marked as "under attack" (only by later queen)in previous step.
def unfill(i, j):
    global chess, mess
    chess[i][j] = 2
    arg = i * n + j + 1
    for a in range(n**2):
        if arg in mess[a]:
            while arg in mess[a]:
                mess[a].remove(arg)
            if not any(mess[a]):
                p = a // n
                q = a % n
                chess[p][q] = 2

# here we randomly choose a starting point for placing the queens so that we have a different arangement on each run.
space = []
for a in range(n):
    Toss = randint(0,n-1)
    while Toss in space:
        Toss = randint(0,n-1)
    space.append(Toss)

#this function is the core, and recursively places the queens.
x = 0
def Quee():
    global chess, mess, x
    for a in range(n):
        if chess[space[x]][a] == 2:
            fill(space[x], a)
            x += 1
            if x < n:
                Quee()
                x -= 1
                for b in range(n):
                    if chess[space[x]][b] == 'Q':
                        unfill(space[x], b)
            else:
                for v in range(n):
                    print(' '.join(chess[v]))
                sys.exit()
        else:
            if a == n - 1:
                for b in range(n):
                    if chess[space[x - 1]][b] == 1:
                        unfill(space[x - 1], b)
                        break
Quee()
