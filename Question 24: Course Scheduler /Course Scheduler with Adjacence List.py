class Solution:
    def canFinish(self, n, prerequisites):
        indegree = [0] * n
        adjList = [[] for _ in range(n)]
        for i in range(len(prerequisites)):
            pair = prerequisites[i]
            indegree[pair[0]] += 1
            adjList[pair[1]].append(pair[0])
        stack = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)
        count = 0
        while len(stack):
            current = stack.pop()
            count += 1
            adj = adjList[current]
            for i in range(len(adj)):
                next = adj[i]
                indegree[next] -= 1
                if indegree[next] == 0:
                    stack.append(next)
        return count == n
    
x = Solution()
x1 = x.canFinish(6, [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]])
print(x1)
