grid = [['-','-','-'],['-','-','-'],['-','-','-']]

def ShowGrid():
    for row in grid:
        print(row[0],row[1],row[2])

def Player1Input():
    inp=input("Player 1 - Enter x,y values:").split(',')
    x,y=int(inp[0]),int(inp[1])
    return x,y

def Player2Input():
    inp=input("Player 2 - Enter x,y values:").split(',')
    x,y=int(inp[0]),int(inp[1])
    return x,y

def IsGameOver():
    

def Main():
    ShowGrid()

    for i in range(0,9):
        if i%2==0:
            x,y=Player1Input()
            grid[x][y]='x'
        else:
            x,y=Player2Input() 
            grid[x][y]='o'     
        ShowGrid()
        IsGameOver()
        
Main()
