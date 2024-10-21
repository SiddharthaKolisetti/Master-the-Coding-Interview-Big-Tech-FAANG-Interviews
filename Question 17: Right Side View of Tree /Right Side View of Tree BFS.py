class Solution:
    def rightSideView(self, root):
        if root == None:
            return []
        result = []
        queue = [root]
        while len(queue):
            length = len(queue)
            count = 0
            while count < length:
                currentNode = queue.pop(0)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                count += 1
            result.append(currentNode.val)
        return result
