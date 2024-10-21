class Solution:
    def countNodes(self, root):
        result = []
        self.DFS(root, 0, result)
        return len(result)
    
    def DFS(self, node, currentLevel, result):
        if node == None:
            return []
        if currentLevel >= len(result):
            result.append(node.val)
        if node.right:
            result.append(node.right.val)
            self.DFS(node.right, currentLevel + 1, result)
        if node.left:
            result.append(node.left.val)
            self.DFS(node.left, currentLevel + 1, result)
