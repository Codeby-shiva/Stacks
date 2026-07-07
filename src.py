# Node class
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


# Class Stack 
class Stack:
    def __init__(self):
        self.head = None
        self.node = 0

    def push(self,value):
        new_node = Node(value)

        if self.head == None:
           self.head = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
            self.node += 1


    def peek(self):
        print(self.head.data)
        return

    def pop(self):
        if self.head == None:
            print("Empty Stack")
            return
        else:
            self.head = self.head.next
            self.node -= 1


    def traverse(self):
        if self.head == None:
            print("Empty Stack")
            return

        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    
    



