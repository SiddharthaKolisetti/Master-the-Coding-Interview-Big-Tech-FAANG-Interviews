class Solution:
    def rightSideView(self, root):
        result = []
        self.DFS(root, 0, result)
        return result
    
    def DFS(self, node, currentLevel, result):
        if node == None:
            return []
        if currentLevel >= len(result):
            result.append(node.val)
        if node.right:
            self.DFS(node.right, currentLevel + 1, result)
        if node.left:
            self.DFS(node.left, currentLevel + 1, result)
