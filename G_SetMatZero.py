class Solution(object):
    def setZeroes(self, matrix):
        
        col0 = 1
        row, col = len(matrix), len(matrix[0])
        
        for i in range(row):
            if matrix[i][0] == 0: col0 = 0
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(row - 1, -1, -1):
            for j in range(col-1, 0, -1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0
        
        
        
"""

Things to remember:

1) traverse the whole matrix, whenever got 0, put zero at the starting of row and column.
2) put mat[i][j] = 0, if mat[i][0] = 0 or mat[0][j] = 0
3) take care of column1 because it can collide with row1 values

"""
