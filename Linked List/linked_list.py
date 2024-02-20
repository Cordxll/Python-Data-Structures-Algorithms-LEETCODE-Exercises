class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node

class LinkedList:
    def __init__(self,value):
        new_node: Node = Node(value)
        self.head: Node = new_node
        self.tail: Node = new_node
        self.length: int = 1
    
    def print_list(self):
        x: Node = self.head
        while x is not None and self.length != 0:
            print(x.value)
            x: Node = x.next

    def append(self, value):
        new_node = Node(value)
        if self.length != 0:
            self.tail.next: Node = new_node
            self.tail: Node = new_node
        else:
            self.tail: Node = new_node
            self.head: Node = new_node
        self.length += 1
    
    def pop(self, value):
        current_node: Node = self.head
        next_node: Node = current_node.next
            
        while next_node != value and next_node != None:
            current_node: Node = current_node.next
            next_node: Node = current_node.next
        
        left_node: Node = current_node
        right_node: Node = left_node.next
        left_node.next: Node = right_node.next
 
    def prepend(self, value):
        
        pass
    def pop_first(self):
        self.head = self.head.next
        
        pass
    def insert(self, value):
        pass
    def remove(self):
        pass
    def lookup_by_index(self):
        pass
    def lookup_by_value(self):
        pass

