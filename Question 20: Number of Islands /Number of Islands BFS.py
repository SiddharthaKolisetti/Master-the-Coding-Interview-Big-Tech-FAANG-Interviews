class Solution:
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        islandcount = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islandcount += 1
                    grid[row][col] = 0
                    queue = []
                    queue.append([row, col])
                    while queue:
                        currentpos = queue.pop(0)
                        currentrow = currentpos[0]
                        currentcol = currentpos[1]
                        for i in range(len(directions)):
                            currentdir = directions[i]
                            nextrow = currentrow + currentdir[0]
                            nextcol = currentcol + currentdir[1]
                            if nextrow < 0 or nextrow >= len(grid) or nextcol < 0 or nextcol >= len(grid[0]):
                                continue
                            if grid[nextrow][nextcol] == '1':
                                queue.append([nextrow, nextcol])
                                grid[nextrow][nextcol] = 0
        return islandcount

x = Solution()
x1 = x.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print(x1)
