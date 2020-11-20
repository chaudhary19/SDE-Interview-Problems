class Solution(object):
    
    def isValidSudoku(self, board):
        return (self.isValidRow(board) and self.isValidCol(board) and self.isValidSquare(board))
    
    def isValidUnit(self, unit):
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))
    
    def isValidRow(self, board):
        for row in board:
            if not self.isValidUnit(row):
                return False
        return True
    
    def isValidCol(self, board):
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False
        return True

    def isValidSquare(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                unit = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isValidUnit(unit):
                    return False
        return True
