class Solution:
    def flatten(self, head):
        if head == None:
            return head
        currentnode = head
        while currentnode != None:
            if currentnode.child == None:
                currentnode = currentnode.next
            else:
                tail = currentnode.child
                while tail.next != None:
                    tail = tail.next
            
                tail.next = currentnode.next
                if tail.next != None:
                    tail.next.prev = tail
                currentnode.next = currentnode.child
                currentnode.next.prev = currentnode
                currentnode.child = None
        return head
