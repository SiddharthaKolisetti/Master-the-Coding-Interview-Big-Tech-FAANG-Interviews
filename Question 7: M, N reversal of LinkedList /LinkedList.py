class Node():
     def __init__(self, data):
         self.data = data
         self.next = None

class Solution:
    def __init__(self):
        self.head = None
        
    def print_LL(self):
        if self.head == None:
            print("LL is empty")
        else:
            temp = self.head
            count = 1
            while temp != None:
                 if count < self.length:
                      print(temp.data, end = ' ---> ')
                      temp = temp.next
                      count +=1
                 elif count == self.length:
                      print(temp.data , end = ' ---> None ')
                      temp = temp.next
            print('\nLength = ' + str(self.length))

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.length = 1
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def insert(self, data, pos):
        new_node = Node(data)
        if pos >= self.length:
            self.append(data)
        elif pos == 0:
            self.prepend(data)
        else:
            temp = self.head
            count = 1
            while temp != None and count < pos:
                temp = temp.next
                count += 1
                
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
    
    def remove(self, pos):
        if self.head == None:
            return "LinkedList is empty"
        if pos > self.length or pos < 0:
            return "Position of node not found in List"
        elif pos == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            temp = self.head
            count = 1
            while temp != None and count < pos:
                temp = temp.next
                count += 1
            temp.next = temp.next.next
            self.length -=1
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr != None:
            nextp = curr.next
            curr.next = prev
            prev = curr
            curr = nextp
        self.head = prev

ll = Solution()
ll.append(30)
ll.append(50)
ll.append(100)
ll.prepend(10)
ll.prepend(20)
ll.prepend(70)
ll.insert(40, 2)
ll.print_LL()
ll.remove(1)
ll.print_LL()
ll.reverse()
ll.print_LL()
