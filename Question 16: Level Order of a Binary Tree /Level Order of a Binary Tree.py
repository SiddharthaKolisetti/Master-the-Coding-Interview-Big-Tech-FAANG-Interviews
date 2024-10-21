class Solution:
    def levelOrder(self, root):
        if root == None:
            return []
        result = []
        queue = [root]
        while len(queue):
            length = len(queue)
            count = 0
            currlevValues = []
            while count < length:
                currentNode = queue.pop(0)
                currlevValues.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                count += 1
            result.append(currlevValues)
        return result
