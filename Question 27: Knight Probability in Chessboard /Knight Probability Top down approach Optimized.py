class Solution:
    def knightProbability(self, n, k, r, c):
        dp = [[[None] * n for _ in range(n)] for _ in range(k + 1)]
        return self.recurse(n, k, r, c, dp)
    
    def recurse(self, n, k, r, c, dp):
        if r < 0 or r >= n or c < 0 or c >= n:
            return 0
        if k == 0:
            return 1
        if dp[k][r][c] is not None:
            return dp[k][r][c]
        directions = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        res = 0
        for d in directions:
            res += self.recurse(n, k - 1, r + d[0], c + d[1], dp) / 8
        dp[k][r][c] = res
        return dp[k][r][c]

x = Solution()
x1 = x.knightProbability(3, 2, 0, 0)
print(x1)
