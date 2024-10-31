from typing import List

class MatrixBundle:
    
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





