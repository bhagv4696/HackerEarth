def isWinner(player_inturn):
    # check horizontal spaces
    for y in range(BOARDWIDTH):
        for x in range(BOARDHEIGHT - 3):
            if grid[x][y] == player_inturn and grid[x+1][y] == player_inturn and grid[x+2][y] == player_inturn and grid[x+3][y] == player_inturn:
                return True

    # check vertical spaces
    for x in range(BOARDHEIGHT):
        for y in range(BOARDWIDTH - 3):
            if grid[x][y] == player_inturn and grid[x][y+1] == player_inturn and grid[x][y+2] == player_inturn and grid[x][y+3] == player_inturn:
                return True

    # check / diagonal spaces
    for x in range(BOARDHEIGHT - 3):
        for y in range(3, BOARDWIDTH):
            if grid[x][y] == player_inturn and grid[x+1][y-1] == player_inturn and grid[x+2][y-2] == player_inturn and grid[x+3][y-3] == player_inturn:
                return True

    # check \ diagonal spaces
    for x in range(BOARDHEIGHT - 3):
        for y in range(BOARDWIDTH - 3):
            if grid[x][y] == player_inturn and grid[x+1][y+1] == player_inturn and grid[x+2][y+2] == player_inturn and grid[x+3][y+3] == player_inturn:
                return True

    return False


def numberOfConnect(player_inturn):
    # check horizontal spaces
    count = 0
    for y in range(BOARDWIDTH):
        for x in range(BOARDHEIGHT - 3):
            if ((grid[x][y] == player_inturn) or (grid[x][y] == 0)) and ((grid[x+1][y] == player_inturn) or (grid[x+1][y] == 0)) and ((grid[x+2][y] == player_inturn) or (grid[x+2][y] == 0)) and ((grid[x+3][y] == player_inturn) or (grid[x+3][y] == 0)):
                count = count + 1

    # check vertical spaces
    for x in range(BOARDHEIGHT):
        for y in range(BOARDWIDTH - 3):
            if ((grid[x][y] == player_inturn) or (grid[x][y] == 0)) and ((grid[x][y+1] == player_inturn) or (grid[x][y+1] == 0)) and ((grid[x][y+2] == player_inturn) or (grid[x][y+2] == 0)) and ((grid[x][y+3] == player_inturn) or (grid[x][y+3] == 0)):
                count = count + 1

    # check / diagonal spaces
    for x in range(BOARDHEIGHT - 3):
        for y in range(3, BOARDWIDTH):
            if ((grid[x][y] == player_inturn) or (grid[x][y] == 0)) and ((grid[x+1][y-1] == player_inturn) or (grid[x+1][y-1] == 0)) and ((grid[x+2][y-2] == player_inturn) or (grid[x+2][y-2] == 0)) and ((grid[x+3][y-3] == player_inturn) or (grid[x+3][y-3] == 0)):
                count = count + 1

    # check \ diagonal spaces
    for x in range(BOARDHEIGHT - 3):
        for y in range(BOARDWIDTH - 3):
            if ((grid[x][y] == player_inturn) or (grid[x][y] == 0)) and ((grid[x+1][y+1] == player_inturn) or (grid[x+1][y+1] == 0)) and ((grid[x+2][y+2] == player_inturn) or (grid[x+2][y+2] == 0)) and ((grid[x+3][y+3] == player_inturn) or (grid[x+3][y+3] == 0)):
                count = count + 1

    return count


def mini_max(player_inturn,depth):
    if player_inturn == player:
        if isWinner(player):
            return sys.maxint
    elif isWinner(player_inturn):
        return -sys.maxint
    elif depth == 2:
        return numberOfConnect(player)-numberOfConnect((player % 2) + 1)

    score = -sys.maxint
    move = -1

    for i in range(BOARDWIDTH):
        if grid[0][i] == 0:
            for j in range(BOARDHEIGHT):
                if grid[j][i] != 0:
                    grid[j - 1][i] = player_inturn
                    total = mini_max((player_inturn % 2) + 1,depth+1)
                    if total > score:
                        score = total
                        move = i
                    grid[j - 1][i] = 0
                    break
                elif j == (BOARDHEIGHT - 1):
                    grid[j][i] = player_inturn
                    total = mini_max((player_inturn % 2) + 1,depth+1)
                    if total > score:
                        score = total
                        move = i
                    grid[j][i] = 0
    return score


import sys
BOARDHEIGHT = 7
BOARDWIDTH = 8

grid = [[0 for i in range(BOARDWIDTH)] for j in range(BOARDHEIGHT)]

for i in range(BOARDHEIGHT):
    temp = raw_input('').split(" ")
    for j in range(BOARDWIDTH):
        grid[i][j] = int(temp[j])
player = int(raw_input(""))

score = -sys.maxint
move = -1
for i in range(BOARDWIDTH):
    if grid[0][i] == 0:
        for j in range(BOARDHEIGHT):
            if grid[j][i] != 0:
                grid[j - 1][i] = player
                total = mini_max((player % 2) + 1,0)
                if total > score:
                    score = total
                    move = i
                grid[j - 1][i] = 0
                break
            elif j == (BOARDHEIGHT - 1):
                grid[j][i] = player
                total = mini_max((player % 2) + 1,0)
                if total > score:
                    score = total
                    move = i
                grid[j][i] = 0
print(move)
