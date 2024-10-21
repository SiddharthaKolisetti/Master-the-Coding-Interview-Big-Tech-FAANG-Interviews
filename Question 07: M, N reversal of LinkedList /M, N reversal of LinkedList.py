class Solution:
    def reverseBetween(self, head, left, right):
        currentpos = 1
        currentnode = head
        start = head
        while currentpos < left:
            start = currentnode
            currentnode = currentnode.next
            currentpos += 1
        newlist = None
        tail = currentnode
        while currentpos >= left and currentpos <= right:
            next = currentnode.next
            currentnode.next = newlist
            newlist = currentnode
            currentnode = next
            currentpos += 1
        
        start.next = newlist
        tail.next = currentnode
        
        if left > 1:
            return head
        else:
            return newlist
