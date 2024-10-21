class Solution:
    def canFinish(self, n, prerequisites):
        in_degree = [0] * n
        for pair in prerequisites:
            in_degree[pair[0]] += 1
        stack = []
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                stack.append(i)
        count = 0
        while stack:
            current = stack.pop()
            count += 1
            for pair in prerequisites:
                if pair[1] == current:
                    in_degree[pair[0]] -= 1
                    if in_degree[pair[0]] == 0:
                        stack.append(pair[0])
        return count == n
        
x = Solution()
x1 = x.canFinish(6, [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]])
print(x1)
