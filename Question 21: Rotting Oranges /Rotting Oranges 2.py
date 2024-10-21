class Solution:
    def orangesRotting(self, grid):
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        rotten = 2
        fresh = 1
        empty = 0
        if len(grid) == 0:
            return 0
        queue = []
        fresh_oranges = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == rotten:
                    queue.append([row, col])
                if grid[row][col] == fresh:
                    fresh_oranges += 1
        cqs = len(queue)
        minutes = 0
        while len(queue) > 0:
            if cqs == 0:
                minutes += 1
                cqs = len(queue)
            co = queue.pop(0)
            cqs -= 1
            row = co[0]
            col = co[1]
            for i in range(len(directions)):
                cd = directions[i]
                nr = cd[0] + row
                nc = cd[1] + col
                if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
                    continue
                if grid[nr][nc] == fresh:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    queue.append([nr, nc])
        if fresh_oranges > 0:
            return -1
        return minutes
        
x = Solution()
x1 = x.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(x1)
