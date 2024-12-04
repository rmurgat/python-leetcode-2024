from typing import List

class MatrixBundle:

    def printPrint(self, matrix: List[List[int]]):
        for row in matrix:
            print (row)

    
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        #check each row
        for row in matrix:
            if len(set(row)) != n: 
                return False

        #check each column
        j = 0
        while j<n:
            column = [row[j] for row in matrix]
            if len(set(column))!=n:
                return False
            j+=1
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        #check each row
        i = 0
        while i<n:
            row = board[i]
            nums = []
            for num in row:
                if num!='.':
                    if num in nums: 
                        return False
                    else:
                        nums.append(num)
            i+=1

        #check each column
        j = 0
        while j<n:
            column = [row[j] for row in board]
            nums = []
            for num in column:
                if num!='.':
                    if num in nums: 
                        return False
                    else:
                        nums.append(num)
            j+=1

        #check each box
        for x in range (3):
            for y in range (3):
                nums = []
                for i in range(x*3,x*3+3):
                    for j in range(y*3,y*3+3):
                        num = board[i][j]
                        if num!=".":
                            if num in nums:
                                return False
                            else:
                                nums.append(num)
        return True
    
    #A sudoku solution must satisfy all of the following rules:
    # 1. Each of the digits 1-9 must occur exactly once in each row.
    # 2. Each of the digits 1-9 must occur exactly once in each column.
    # 3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    # The '.' character indicates empty cells.
    def solveSudoku_1(self, board: List[List[str]]) -> None:
        rows = []
        columns = []
        d = {}
        keys2process=[]

        def getRow(board:  List[List[str]], row:int) -> List[str]:
            res = []
            for col in range (0, 9):
                if board[row][col]!='.':
                    res.append(board[row][col])
            return res
        
        def getColumn(board:  List[List[str]], column:int) -> List[str]:
            res = []
            for row in range (0, 9):
                if board[row][column]!='.':
                    res.append(board[row][column])
            return res

        def getBoxOptions(board: List[List[str]], i, j) -> None:
            res = ['1','2','3','4','5','6','7','8','9']

            for row in range (i,i+3):
                for col in range (j, j+3):
                    if board[row][col]!='.':
                        res.remove(board[row][col])

            for row in range (i, i+3):
                for col in range (j, j+3):
                    if board[row][col]=='.':
                        options = [opt for opt in res if opt not in getRow(board,row)]
                        options = [opt for opt in options if opt not in getColumn(board,col)]
                        d[(row, col)] = options
                        keys2process.append((row, col))

        # Step 1: generating options by empty cell
        for i in range(0,len(board), 3):
            for j in range(0,len(board[i]), 3):
                getBoxOptions(board, i, j)

        # Step 2: taking values with unique option
        #print ("[STARTING...]")
        #print ("keys2process: ", keys2process)
        #print ("dictionary:", d)

        
        counter = 0
        while len(keys2process)>0:

            #print ("keys2process: ", keys2process)
            #print ("dictionary:", d)

            for key in keys2process:
                options = d[key]
                if len(options)==1:
                    option = options[0]
                    board[key[0]][key[1]] = option
                    d.clear()
                    keys2process.clear()
                    
                    for i in range(0,len(board), 3):
                        for j in range(0,len(board[i]), 3):
                            getBoxOptions(board, i, j)


        #print ("ENDING...")
        #print ("keys2process: ", keys2process)
        #print ("dictionary:", d)
        
        return

    #A sudoku solution must satisfy all of the following rules:
    # 1. Each of the digits 1-9 must occur exactly once in each row.
    # 2. Each of the digits 1-9 must occur exactly once in each column.
    # 3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
    # The '.' character indicates empty cells.
    def solveSudoku_2(self, board: List[List[str]]) -> None:
        columns = []
        rows = []
        d = {}
        cell2deal = []

        def getBoxOptions(board: List[List[str]], boxcounter, i, j) -> None:
            res = ['1','2','3','4','5','6','7','8','9']

            for row in range (i,i+3):
                for col in range (j, j+3):
                    if board[row][col]!='.':
                        res.remove(board[row][col])

            for row in range (i, i+3):
                for col in range (j, j+3):
                    if board[row][col]=='.':
                        options = [opt for opt in res if opt not in rows[row]]
                        options = [opt for opt in options if opt not in columns[col]]
                        d[(row, col, boxcounter)] = options
                        cell2deal.append((row, col, boxcounter))

        # Step 1: generating rows and columns
        for i in range (9):
            rows.append([x for x in board[i] if x!='.'])
            columns.append([x[i] for x in board if x[i]!='.'])

        # Step 2: set chances por each box
        boxcounter = 0
        for boxi in range(0,len(board), 3):
            for boxj in range(0,len(board[i]), 3):
                getBoxOptions(board, boxcounter, boxi, boxj)
                boxcounter+=1


        # Step 3: deading with each cell
        lastsize = len(cell2deal)
        while lastsize > 0:
            print ("cell2deal:",cell2deal)
            for key in cell2deal:
                options = d.get(key, None)
                #print ("to process:", key, options)
                if options and len(options)==1:
                    #print ("to process", key)
                    option = options[0]
                    board[key[0]][key[1]] = option
                    del d[key]

                    # Step 3.1: remove option from row or column or box
                    for tmp in cell2deal:
                        if tmp[0]==key[0] or tmp[1]==key[1] or tmp[2]==key[2]:
                            options1 = d.get(tmp, None)
                            if options1 and option in options1:
                                options1.remove(option)
                                d[tmp]=options1

                    # Step 3.4: remove from cell2deal
                    cell2deal.remove(key)
            if lastsize == len(cell2deal): break
            lastsize = len(cell2deal)
        print ("d:",d)

        return
    
    # https://leetcode.com/problems/rotate-image/
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        # Step 1: transpose the matrix
        for i in range (N):
            for j in range (i+1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            row.reverse()

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass