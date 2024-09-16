class Zigzag:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1: return s
        re = ""
        matrix = [[' '] * len(s) for _ in range(numRows)]
        col = 0
        row = 0
        forward = True
        
        for car in s:
            print ("i,j:[",row,",",col,"]=",car)
            matrix[row][col] = car
            if forward:
                if row == numRows - 1:
                    row = row - 1
                    col = col + 1
                    forward = False
                else:
                    row = row + 1
            else:
                if row == 0:
                    row = 1
                    forward = True
                else:
                    row = row - 1
                    col = col + 1

        for row in matrix:
            print(row)

        for row in matrix:
            for car in row:
                if car!=' ': re = re + car

        return re