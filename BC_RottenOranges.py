class Solution(object):
    def orangesRotting(self, grid):
        
        row, col = len(grid), len(grid[0])
        fresh, rotten = set(), set()
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.add((i, j))
        
        timer = 0
        position = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while fresh:
            if not rotten:
                return -1
            rotten = {(i+dx, j+dy) for i, j in rotten for dx, dy in position if (i+dx, j+dy) in fresh}
            fresh -= rotten
            timer += 1
        
        return timer
