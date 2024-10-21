class Solution:
    def detectCycle(self, head):
        hare = head
        tortoise = head
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if tortoise == hare:
                break
        if hare == None or hare.next == None:
            return None
        p1 = head
        p2 = tortoise
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1 
