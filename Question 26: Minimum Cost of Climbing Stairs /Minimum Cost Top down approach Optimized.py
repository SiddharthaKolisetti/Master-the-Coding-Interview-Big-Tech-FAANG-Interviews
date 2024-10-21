class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [None] * n
        return min(self.minCost(n-1,cost, dp), self.minCost(n-2, cost, dp))
        
    def minCost(self, i, cost, dp):
        if i < 0:
            return 0
        if i == 0 or i == 1:
            return cost[i]
        if dp[i] is not None:
            return dp[i]
        dp[i] = cost[i] + min(self.minCost(i-1, cost, dp), self.minCost(i-2, cost, dp))
        return dp[i]

x = Solution()
x1 = x.minCostClimbingStairs([10, 15, 20])
print(x1)
