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
        self.reward = 0
        self.current_inrow = 0

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

        if column < 7 and row < 6:
            if self.grid[column][row] == self.num:
                inrow += 1
                self.Update_inrow(inrow)
                if inrow == 4:
                    self.won = True
                else:
                    self.CheckDiagonal(row, column, inrow, left)


    def CheckVertical(self, row, column, inrow):
        row -= 1
        if row != -1:
            if self.grid[column][row] == self.num:
                inrow += 1
                self.Update_inrow(inrow)
                if inrow == 4:
                    self.won = True
                else:
                    self.CheckVertical(row, column, inrow)


    def CheckHorizontal(self, row, column, inrow):
        column += 1
        if column != 7:
            if self.grid[column][row] == self.num:
                inrow += 1
                self.Update_inrow(inrow)
                if inrow == 4:
                    self.won = True
                else:
                    self.CheckHorizontal(row, column, inrow)

    def Update_inrow(self, inrow):
        if inrow > self.current_inrow:
            self.current_inrow = inrow


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
        self.current_inrow = 0
        column = int(input("1-7: "))
        column -= 1
        self.Drop(column)
        self.Display()
        self.PieceWinCheck()
        if self.won == True:
            print("player ", self.num, " has won")
            self.Reset(False)
        else:
            print(self.current_inrow)
            self.SwapTurn()
            self.Turn()
            

    def Grid_Reset(self):
        for i in range(7):
            for u in range(6):
                self.grid[i][u] = 0

        self.won = False
        self.inrow = 0
        self.reward = 0

    def Reset(self, action):
        if action == True:
            self.action()
        else:
            Turn()

    
    def Calc_Reward(self):
        if self.won == True:
            self.reward = 12
        elif self.current_inrow == 2:
            self.reward = 1
        elif self.current_inrow == 3:
            self.reward = 4 
        

    def Action(self, column):
        self.current_inrow = 0
        column -= 1
        self.Drop(column)
        self.Display()
        self.PieceWinCheck()
        self.Calc_Reward()
        if self.won == True:
            print("player ", self.num, " has won")
            self.Grid_Reset()
            return self.grid
            return self.reward
            self.Reset(True)
        else:
            return self.reward
            self.SwapTurn()
            self.action()
        
        
            
episode = Grid()
#episode.Turn()
