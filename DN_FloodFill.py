from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        
        row, col = len(image), len(image[0])
        visited = [[False for i in range(col)] for j in range(row)]
        
        Q = deque()
        Q.append((sr, sc))
        color = image[sr][sc]
        
        while Q:
            Row, Col = Q.popleft()
            # print(row, col)
            if visited[Row][Col]:
                continue
            visited[Row][Col] = True
            if image[Row][Col] == color:
                
                image[Row][Col] = newColor
                
                r, c = Row, Col-1
                
                if 0 <= r < row and 0 <= c < col and not visited[r][c] and image[r][c] == color:
                    Q.append((r, c))
                    
                    
                r, c = Row, Col+1
                
                if 0 <= r < row and 0 <= c < col and not visited[r][c] and image[r][c] == color:
                    Q.append((r, c))
                    
                    
                r, c = Row-1, Col
                
                if 0 <= r < row and 0 <= c < col and not visited[r][c] and image[r][c] == color:
                    Q.append((r, c))
                    
                    
                r, c = Row+1, Col
                
                if 0 <= r < row and 0 <= c < col and not visited[r][c] and image[r][c] == color:
                    Q.append((r, c))
                    
        
        return image
                    
                
