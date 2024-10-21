class Solution:
    def dfs(self, grid, currentRow, currentCol):
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        if currentRow < 0 or currentRow >= len(grid) or currentCol < 0 or currentCol >= len(grid[0]):
            return
        if grid[currentRow][currentCol] == '1':
            grid[currentRow][currentCol] = 0
            for currentDir in directions:
                row = currentDir[0]
                col = currentDir[1]
                self.dfs(grid, currentRow + row, currentCol + col)

    def numIslands(self, grid):
        if not grid:
            return 0
        islandCount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islandCount += 1
                    self.dfs(grid, row, col)
        return islandCount

x = Solution()
x1= x.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])
print(x1)
