class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr != None:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp
        self.head = prev
        return prev
