class Solution:
    def canFinish(self, n, prerequisites):
        adjList = [[] for _ in range(n)]
        for pair in prerequisites:
            adjList[pair[1]].append(pair[0])
        for v in range(n):
            queue = []
            seen = {}
            for i in range(len(adjList[v])):
                queue.append(adjList[v][i])
            while queue:
                current = queue.pop(0)
                seen[current] = True
                if current == v:
                    return False
                adjacent = adjList[current]
                for i in range(len(adjacent)):
                    next_vertex = adjacent[i]
                    if not seen.get(next_vertex):
                        queue.append(next_vertex)
        return True
