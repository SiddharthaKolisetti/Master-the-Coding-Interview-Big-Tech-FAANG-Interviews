class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.prev = None
            self.length = 1
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            self.length += 1
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
    
    def insert(self, data, pos):
        new_node = Node(data)
        if pos >= self.length:
            self.append(data)
        if pos == 0:
            self.prepend(data)
        else:
            temp = self.head
            count = 1
            while temp != None and count < pos:
                temp = temp.next
                count +=1
            new_node.prev = temp
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
    
    def remove(self, pos):
        if self.head == None:
            print("Doubly Linked List is empty")
        if pos > self.length or pos < 0:
            print("Node not found in Doubly Linked List")
        if pos == 0:
            self.head = self.head.next
            self.head.next.prev = None
            self.length -= 1
        else:
            temp = self.head
            count = 1
            while temp != None and count < pos:
                temp = temp.next
                count += 1
            temp.prev = temp.next.prev
            temp.next = temp.next.next
            self.length -= 1
    
    def print_LL(self):
        if self.head == None:
            print("Doubly LinkedList is empty")
        else:
            temp = self.head
            count = 1
            while temp != None and count == 1:
                print('None ---> ',temp.data, end = ' <-===-> ')
                temp= temp.next
                count += 1
            while temp != None and count < self.length:
                print(temp.data, end = ' <-===-> ')
                temp = temp.next
                count += 1
            while temp != None and count == self.length:
                print(temp.data, end = ' ---> None')
                temp = temp.next
            print('\nLength = ' + str(self.length))

    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node != None:
            nextp = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = nextp
        self.head = prev_node
    
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(40)
dll.insert(50, 3)
dll.remove(0)
dll.remove(1)
dll.print_LL()
dll.reverse()
dll.print_LL()
