grid = None


def InitializeGrid():
    global grid
    grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    return


def ShowGrid():
    global grid
    for row in grid:
        print(row[0], row[1], row[2])


def Player1Input():
    x = -1
    y = -1
    while not ValidateInput(x, y):
        inp = input("Player 1 Enter coma separated x, y values:")
        x, y = ProcessInput(inp)
    return x, y


def Player2Input():
    x = -1
    y = -1
    while not ValidateInput(x, y):
        inp = input("Player 2 Enter coma seperated x, y values:")
        x, y = ProcessInput(inp)
    return x, y


def ProcessInput(inp):
    inp = inp.split(',')
    x = int(inp[0])
    y = int(inp[1])
    return x, y


def ValidateInput(x, y):
    global grid
    if x < 0 or y < 0 or x > 2 or y > 2:
        if x != -1 and y != -1:
            print("Player please enter the values in range 0 to 2")
        return False
    elif grid[x][y] != '-':
        print("Provided coordinates are filled, enter different coordinates")
        return False
    return True


def DidSomeoneWin(ch):
    global grid
    if(grid[0][0] == ch and grid[1][1] == ch and grid[2][2] == ch):
        return True
    elif(grid[0][2] == ch and grid[1][1] == ch and grid[2][0] == ch):
        return True

    for i in range(0, 3):
        if(grid[i][0] == ch and grid[i][1] == ch and grid[i][2] == ch):
            return True
        elif(grid[0][i] == ch and grid[1][i] == ch and grid[2][i] == ch):
            return True
    return False

def ModifyGrid(x, y, sym):
    global grid
    grid[x][y] = sym


def IsGameOver():
    if DidSomeoneWin('X'):
        print("Congratulations Player 1")
        return True
    elif DidSomeoneWin('O'):
        print("Congratulations Player 2")
        return True
    return False


def main():
    InitializeGrid()
    move = 0
    x = -1
    y = -1
    isPlayer1Turn = True
    while(move < 9):
        ShowGrid()
        if isPlayer1Turn:
            x, y = Player1Input()
            ModifyGrid(x, y, 'X')
            isPlayer1Turn = False
        else:
            x, y = Player2Input()
            ModifyGrid(x, y, 'O')
            isPlayer1Turn = True
        if IsGameOver():
            return
        move += 1
    print("Game Drawn! Well played both the players")


main()
