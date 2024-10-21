class Solution:
    def WAG(self, grid):
        wall = -1
        gate = 0
        empty = 2147483647
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == gate:
                    self.traverse(grid, row, col, 0)
        return grid
    
    def traverse(self, grid, row, col, cs):
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or cs > grid[row][col]:
            return
        grid[row][col] = cs
        for i in range(len(directions)):
            cd = directions[i]
            self.traverse(grid, row + cd[0], col + cd[1], cs + 1)
            
x = Solution()
INF = 2147483647
x1 = x.WAG([[INF, -1, 0, INF],
[INF, INF, INF, -1],
[INF, -1, INF, -1],
[0, -1, INF, INF]])
for i in x1:    
    print(i)
