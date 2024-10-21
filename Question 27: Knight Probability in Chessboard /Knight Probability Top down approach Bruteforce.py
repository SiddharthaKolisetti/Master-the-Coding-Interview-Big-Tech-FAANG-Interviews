class Solution:
    def knightProbability(self, n, k, r, c):
        directions = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        if r < 0 or r >= n or c < 0 or c >=n:
            return 0
        if k == 0:
            return 1
        res = 0
        for i in range(len(directions)):
            d = directions[i]
            res += self.knightProbability(n, k-1, r + d[0], c + d[1]) / 8
        return res

x = Solution()
x1 = x.knightProbability(3, 2, 0, 0)
print(x1)
