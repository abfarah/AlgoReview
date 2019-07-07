#Only for use in Python 2.6.0a2 and later
from __future__ import print_function
import sys
sys.path.append( '.' )
sys.path.append( '../linkedList' )

from linkedList import LinkedList

class ArrayStack:
    def __init__(self, data=None):
        self.stack = [None] * 10 if data is None else [data] + [None] * 9
        self.size = 1 if data is not None else 0
        self.top = 0 if data is not None else -1

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack[self.top]
    
    def push(self, x):
        self.top += 1
        if self.top > len(self.stack)-1:
            self.resize()
        self.stack[self.top] = x
        self.size += 1
        self.printStack()

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        self.top -= 1
        self.size -= 1
        self.printStack()
        return self.stack[self.top+1]
    
    def printStack(self):
        print("Stack is:", end=" ")
        for i in range(self.size):
            print(self.stack[i], end=" ")
        print("")

    def resize(self):
        newArr = [None] * (len(self.stack)*2)
        for i in range(0, len(self.stack)):
            newArr[i] = self.stack[i]
        self.stack = newArr

class LinkedListStack:
    def __init__(self, data=None):
        self.stack = LinkedList(data)
        self.size = self.stack.size

    def isEmpty(self):
        if self.size <= 0:
            return True
        return False

    def peek(self):
        return self.stack.head

    def push(self, x):
        self.stack.insertHead(x)
        self.size += 1

    def pop(self):
        x = self.stack.head
        self.stack.deleteHead()
        return x

    def printStack(self):
        print("Stack", end="")
        self.stack.printList()

