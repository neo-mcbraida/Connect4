class Grid:

    def __init__(self):
        self.num = 1
        self.grid = [[0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0]]
        self.won = False

    def Drop(self, column): 
        i = 0
        for i in range(6):
            if self.grid[column][i] != 0:
                self.grid[column][i-1] = self.num
                break
            elif i == 5:
                self.grid[column][i] = self.num
                
    def CheckDiagonal(self, row, column, inrow, left):#left = -1, right = 1, up 1, down -1
        column += left
        row -= 1

        if column < 7 and column > -1 and row < 6 and row > -1:
            if self.grid[column][row] == self.num:
                inrow += 1
                if inrow == 4:
                    self.won = True
                else:
                    self.CheckDiagonal(row, column, inrow, left)

    def CheckVertical(self, row, column, inrow):
        row -= 1
        if row != -1:
            if self.grid[column][row] == self.num:
                inrow += 1
                if inrow == 4:
                    self.won = True
                else:
                    self.CheckVertical(row, column, inrow)

    def CheckHorizontal(self, row, column, inrow):
        column += 1
        if column != 7:
            if self.grid[column][row] == self.num:
                inrow += 1
                if inrow == 4:
                    self.won = True
                else:
                    self.CheckHorizontal(row, column, inrow)

    def PieceWinCheck(self):
        for i in range(7):
            for u in range (6):
                if self.grid[i][u] == self.num:
                    self.CheckDiagonal(u, i, 1, -1)
                    self.CheckDiagonal(u, i, 1, 1)
                    self.CheckHorizontal(u, i, 1)
                    self.CheckVertical(u, i, 1)

    def SwapTurn(self):
        if self.num == 1:
            self.num = 2
        else:
            self.num = 1

    def Display(self):
        grid = self.grid
        print(grid[0][0], grid[1][0], grid[2][0], grid[3][0], grid[4][0], grid[5][0], grid[6][0])
        print(grid[0][1], grid[1][1], grid[2][1], grid[3][1], grid[4][1], grid[5][1], grid[6][1])
        print(grid[0][2], grid[1][2], grid[2][2], grid[3][2], grid[4][2], grid[5][2], grid[6][2])
        print(grid[0][3], grid[1][3], grid[2][3], grid[3][3], grid[4][3], grid[5][3], grid[6][3])
        print(grid[0][4], grid[1][4], grid[2][4], grid[3][4], grid[4][4], grid[5][4], grid[6][4])
        print(grid[0][5], grid[1][5], grid[2][5], grid[3][5], grid[4][5], grid[5][5], grid[6][5])

    def Turn(self):
        column = (int(input("enter a column"))) - 1
        self.Drop(column)
        self.Display()
        self.PieceWinCheck()
        print(self.won)
        if self.won == True:
            print("player ", self.num, " has won")
        else:
            self.SwapTurn()
            self.Turn()
            
    def GetState(self):
        temp = self.grid.copy()
        for row in temp:
            for spot in row:
                if spot == 0:
                    spot = 0.1
                if spot == 2:
                    spot = -1
        temp = temp[0] + temp[1] + temp[2] + temp[3] + temp[4] + temp[5] + temp[6]
        return temp

game = Grid()
game.Turn()
