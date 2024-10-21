class Solution:
    def numOfMinutes(self, n, headID, manager, informTime):
        adjList = [[] for i in manager]
        for e in range(n):
            m = manager[e]
            if m == -1:
                continue
            adjList[m].append(e)
        return self.traverse(headID, adjList, informTime)
        
    def traverse(self, currentID, adjList, informTime):
        if len(adjList[currentID]) == 0:
            return 0
        maxi = 0
        sub = adjList[currentID]
        for i in range(len(sub)):
            maxi = max(maxi, self.traverse(sub[i], adjList, informTime))
        return maxi + informTime[currentID]
