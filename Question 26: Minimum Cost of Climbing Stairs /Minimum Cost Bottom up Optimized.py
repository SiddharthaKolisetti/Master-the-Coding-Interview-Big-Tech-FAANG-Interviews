class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [None] * n
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])
        
x = Solution()
x1 = x.minCostClimbingStairs([10, 15, 20])
print(x1)
