class Solution(object):
    def solveNQueens(self, n):
        
        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            for c in xrange(n):
                if isValid(r, c):
                    board[r][c] = 'Q'
                    backtrack(r+1)
                    board[r][c] = '.'
        
        def isValid(r, c):
            
            for i in xrange(r):
                for j in range(n):
                    if board[i][j] == 'Q' and (j == c or i-j == r-c or i+j == r+c):
                        return False
            return True
        
        res = []
        board = [['.' for i in range(n)] for j in range(n)]
        backtrack(0)                   # start from 0th row
        return res
        
        
        
# ---------------------------------------------------------------------------------------------------
# optimzed -----------
# ----------------
# ------------
# --------

class Solution(object):
    def solveNQueens(self, n):
        
        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            else:
                for c in xrange(n):
                    if c not in col and r-c not in diag and r+c not in off_diag:
                        col.add(c)
                        diag.add(r-c)
                        off_diag.add(r+c)
                        board[r][c] = 'Q'
                        backtrack(r+1)
                        board[r][c] = '.'
                        off_diag.remove(r+c)
                        diag.remove(r-c)
                        col.remove(c)
                        
        
        res = []
        board = [['.' for i in xrange(n)] for j in xrange(n)]
        diag = set()
        off_diag = set()
        col = set()
        backtrack(0)
        return res
