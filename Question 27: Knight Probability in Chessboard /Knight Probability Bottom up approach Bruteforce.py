class Solution:
    def knightProbability(self, n, k, r, c):
        directions = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        dp[0][r][c] = 1
        for step in range(1, k+1):
            for row in range(n):
                for col in range(n):
                    for i in range(len(directions)):
                        d = directions[i]
                        pr = row + d[0]
                        pc = col + d[1]
                        if pr >= 0 and pr < n and pc >= 0 and pc < n:
                            dp[step][row][col] += dp[step - 1][pr][pc] / 8
        res = 0
        for i in range(n):
            for j in range(n):
                res += dp[k][i][j]
        return res
        
x = Solution()
x1 = x.knightProbability(3, 2, 0, 0)
print(x1)
