class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        self.tail = self.head

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self):
        current = self.head
        while current.next is not None and current.next != self.tail:
            current = current.next
        if current.next is not None:
            current.next = None
            self.tail = current

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)



# Stack.py 


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is Empty")
