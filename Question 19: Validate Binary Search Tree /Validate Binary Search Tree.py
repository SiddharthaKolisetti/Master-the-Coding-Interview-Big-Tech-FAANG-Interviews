class Solution:
    def isValidBST(self, root):
        if root == None:
            return True
        return self.DFS(root, -float('inf'), float('inf'))

    def DFS(self, node, min, max):
        if node.val <= min or node.val >=max:
            return False
        if node.left:
            if self.DFS(node.left, min, node.val) == False:
                return False
        if node.right:
            if self.DFS(node.right, node.val, max) == False:
                return False
        return True
