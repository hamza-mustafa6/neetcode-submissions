class Solution:
    from collections import deque

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.bfs(i,j, grid)
                    count+=1
        return count

    def bfs(self, i:int, j:int, grid: List[List[str]]):
        queue = deque()
        queue.append((i, j))
        grid[i][j] = "2"
        cols = len(grid[0])
        rows = len(grid)
        while queue:
            (x,y) = queue.popleft()
            if x-1 >= 0:
                if grid[x-1][y] == "1":
                    queue.append((x-1,y))
                    grid[x-1][y] = "2"
            if y-1 >= 0:
                if grid[x][y-1] == "1":
                    queue.append((x,y-1))
                    grid[x][y-1] = "2"
            if x+1 < rows:
                if grid[x+1][y] == "1":
                    queue.append((x+1,y))
                    grid[x+1][y] = "2"
            if y+1 < cols:
                if grid[x][y+1] == "1":
                    queue.append((x,y+1))
                    grid[x][y+1] = "2"

