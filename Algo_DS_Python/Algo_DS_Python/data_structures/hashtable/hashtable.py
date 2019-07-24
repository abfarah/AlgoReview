from __future__ import print_function
import sys
sys.path.append( '.' )
sys.path.append( '../linkedList' )

from linkedList import LinkedList

class HashWChaining:
    def __init__(self):
        self.hashtable = [LinkedList() for _ in range(10)]

    def isEmpty(self):
        for i in self.hashtable:
            if i.size >0:
                return False
        return True

    def hashItem(self,x):
        return hash(x) % len(self.hashtable)

    def get(self, key):
        h = self.hashItem(key)
        if self.hashtable[h].head == None:
            return None
        if self.hashtable[h].size == 1 and self.hashtable[h].head.data[0] == key:
            return self.hashtable[h].head.data[1]
        temp = self.hashtable[h].head
        count = 1
        while count <= self.hashtable[h].size:
            if temp.data[0] == key:
                return temp.data[1]
            temp = temp.next
            count +=1
        return None

    def insert(self, key, value):
        h = self.hashItem(key)
        self.hashtable[h].insertHead([key, value])

    def delete(self, key):
        h = self.hashItem(key)
        if self.hashtable[h].head == None:
            return None
        if self.hashtable[h].head.data[0] == key:
            self.hashtable[h].deleteHead()
        temp = self.hashtable[h].head
        while temp.next != None:
            if temp.next.data[0] == key:
                if temp.next.next == None:
                    self.hashtable[h].deleteTail()
                temp2 = temp.next
                temp.next = temp2.next
                break
            temp = temp.next

    def displayTable(self):
        count = 0
        for i in self.hashtable:
            print("Hash", end="")
            i.printList()

