class Solution:
    def countNodes(self, root):
        if root == None:
            return 0
        queue = [root]
        result = []
        while len(queue):
            length = len(queue)
            currentnode = queue.pop(0)
            if currentnode.left:
                queue.append(currentnode.left)
            if currentnode.right:
                queue.append(currentnode.right)
            result.append(currentnode.val)
        return len(result)
