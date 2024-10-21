class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        dp1 = cost[0]
        dp2 = cost[1]
        for i in range(2, n):
            current = cost[i] + min(dp1, dp2)
            dp1 = dp2
            dp2 = current
        return min(dp1, dp2)

x = Solution()
x1 = x.minCostClimbingStairs([10, 15, 20])
print(x1)
