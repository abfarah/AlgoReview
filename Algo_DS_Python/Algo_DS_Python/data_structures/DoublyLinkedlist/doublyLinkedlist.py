#Only for use in Python 2.6.0a2 and later
from __future__ import print_function

class Node:
    def __init__(self, x):
        self.data = x
        self.prev = None
        self.next = None

class DoublyLinkedlist:
    def __init__(self, x=None):
        self.head = None if x is None else Node(x)
        self.size = 0 if x is None else 1
        self.tail = None if x is None else self.head

    def insertHead(self, x):
        temp = Node(x)
        if self.head == None:
            self.head = temp
            self.tail = temp
            self.size += 1
        else:
            self.head.prev = temp
            temp.next = self.head
            self.head = temp
            self.size += 1

    def deleteHead(self):
        if self.head != None:
            self.head = self.head.next
            if self.head != None:
                self.head.prev.next = None
                self.head.prev = None
            self.size -= 1
        self.printList()

    def printList(self):
        temp = self.head
        print("List is: ", end="")
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print("")

    def printRecursive(self):
        print("List is: ", end="")
        if self.head == None:
            print("empty")
            return None
        self.printWRecursive(self.head)
        print("")

    def printWRecursive(self, n):
        if n == None:
            return None
        print(n.data, end=" ")
        self.printWRecursive(n.next)

    def printReverseRecursive(self):
        print("List is: ", end="")
        if self.head == None:
            print("empty")
            return None
        self.printWReverseRecursive(self.head)
        print("")

    def printWReverseRecursive(self, n):
        if n == None:
            return None
        self.printWReverseRecursive(n.next)
        print(n.data, end=" ")

    def insert(self, x, i):
        n = Node(x)
        temp = self.head
        if temp == None or i <= 1:
            self.insertHead(x)
        else:
            count = 1
            while count < i-1 and temp.next != None:
                temp = temp.next
                count +=1
            n.next = temp.next
            n.prev = temp
            temp.next = n
            if n.next == None:
                self.tail = n
            self.size += 1
        self.printList()

    def push(self, x):
        if self.head == None:
            self.insertHead(x)
            return None
        n = Node(x)
        temp = self.tail
        self.tail.next = n
        n.prev = self.tail
        self.tail = n
        self.size +=1
        self.printList()

    def delete(self, i):
        if i > self.size or self.head == None:
            return None
        if i <= 1:
            self.deleteHead()
            return None
        if i == self.size:
            self.deleteTail()
            return None

        temp = self.head
        count = 1
        while count < i-1:
            temp = temp.next
            count += 1
        temp2 = temp.next
        temp.next = temp2.next
        temp2.next.prev = temp2.prev
        temp2.next = None
        temp2.prev = None
        self.size -= 1
        self.printList()

    def deleteTail(self):
        if self.head == None:
            return
        temp = self.tail.prev
        temp.next = None
        self.tail.prev = None
        self.tail = temp
        self.size -= 1
        self.printList()

    def search(self, x):
        if self.size < 1:
            return None
        if self.size == 1 or self.head.data == x:
            return self.head
        temp = self.head
        count = 1
        while temp.next != None and count <= self.size:
            if temp.data == x:
                return temp
            temp = temp.next
            count += 1

    def reverseIterative(self):
        if self.head == None:
            print("no nodes in list")
            return None
        current = self.head
        prev = None
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        self.printList()

    def reverseRecursive(self):
        if self.head == None:
            print("no nodes in list")
            return None
        self.reverseWRecursive(self.head)
        self.printList()

    def reverseWRecursive(self, n):
        if n.next == None:
            self.head = n
            return None
        self.reverseWRecursive(n.next)
        temp = n.next
        temp.next = n
        n.next = None
