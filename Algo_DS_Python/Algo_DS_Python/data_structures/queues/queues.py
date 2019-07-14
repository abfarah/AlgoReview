#Only for use in Python 2.6.0a2 and later
from __future__ import print_function
import sys
sys.path.append( '.' )
sys.path.append( '../linkedList' )

from linkedList import LinkedList

class ArrayQueue:
    def __init__(self, data=None):
        self.queue = [None] * 10 if data is None else [data] + [None] * 9
        self.size = 1 if data is not None else 0
        self.front = 0 if data is not None else -1
        self.rear = 0 if data is not None else -1

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def enqueue(self, x):
        n = len(self.queue)
        if (self.rear+1)%n == self.front:
            print("Queue is full")
            return None
        elif self.isEmpty():
            self.front, self.rear = 0, 0
        else:
            self.rear = (self.rear+1)%n
        self.queue[self.rear] = x

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        elif self.front == self.rear:
            x = self.queue[self.front]
            self.front, self.rear = -1, -1
        else:
            x = self.queue[self.front]
            self.front = (self.front+1)%len(self.queue)
        return x

    def peak(self):
        return self.queue[self.front]

    def printQueue(self):
        print("Queue is: ", end="")
        i = self.front
        while i != self.rear+1:
            print(self.queue[i], end= " ")
            i+=1
        print("")


class linkedListQueue:
    def __init__(self, data=None):
        self.queue = LinkedList(data)
        self.size = self.queue.size

    def isEmpty(self):
        if self.size <= 0:
            return True
        return False

    def enqueue(self, x):
        self.queue.insert(x)
        self.size += 1

    def dequeue(self):
        x = self.queue.head
        self.queue.deleteHead()
        return x

    def peak(self):
        return self.queue.head.data

    def printQueue(self):
        print("Queue", end="")
        self.queue.printList()


l = linkedListQueue()
l.enqueue(3)
l.enqueue(5)
l.enqueue(4)
l.enqueue(7)
l.enqueue(8)
l.dequeue()
l.dequeue()
print(l.peak())
