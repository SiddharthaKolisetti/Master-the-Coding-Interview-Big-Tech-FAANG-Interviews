class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = []
        fresh_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_count += 1
        minutes_elapsed = 0
        while queue:
            i, j, minutes = queue.pop(0)
            minutes_elapsed = max(minutes_elapsed, minutes)
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    queue.append((ni, nj, minutes + 1))
                    fresh_count -= 1
        return minutes_elapsed if fresh_count == 0 else -1

x = Solution()
x1 = x.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(x1)
