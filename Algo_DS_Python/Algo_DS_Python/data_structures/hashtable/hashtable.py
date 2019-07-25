from __future__ import print_function
import sys
sys.path.append( '.' )
sys.path.append( '../linkedList' )

from linkedList import LinkedList
from random import randint

class HashWChaining:
    def __init__(self):
        self.hashtable = [LinkedList() for _ in range(10)]
        self.r = randint(0, 100)

    def isEmpty(self):
        for i in self.hashtable:
            if i.size >0:
                return False
        return True

    def hashItem(self,x):
        return (self.r *hash(x)) % len(self.hashtable)

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

    def printTable(self):
        count = 0
        for i in self.hashtable:
            print("Hash", end="")
            i.printList()

class hashWOpenAddressing:
    def __init__(self):
        self.hashtable = [None] * 10
        self.r = randint(1, 100)
    
    def isEmpty(self):
        for i in self.hashtable:
            if i != None:
                return False
        return True

    def hashItem(self,x,i):
        return (self.r *hash(x)) % len(self.hashtable)+i

    def insert(self, key, value):
        count = 0
        isInserted = True
        while count <= 
            h = self.hashItem(key, count)
            if self.hashtable[h] != None and self.hashtable[h] != "DeletedFile":
                self.hashtable[h] == [key, value]
                isInserted = False
            else:
                count+=1

    def get(self, x):
        count = 0
        while isFound:
            h = self.hash(x, count)
            if self.hashtable[h] == None:
                return None
            elif self.hashtable[h][0] == x:
                return self.hashtable[h][1]
            count+=1

    def delete(self, x):
        count = 0
        isFound = False
        while isFound:
            h = self.hashItem(key, count)
            if self.hashtable[h] == None:
                return None
            elif self.hashtable[h][0] == x:
                self.hashtable[h] == "DeletedFile"
            count+=1
            
    
    def printTable(self):
        for i in self.hashtable:
            if i == None:
                print("None")
            elif i == "DeletedFile":
                print("Deleted file****")
            else:
                print("Key: " + str(i[0]) + " Value: " + str(i[1]))



l = hashWOpenAddressing()
l.insert(8, "dfa")
l.insert(4, "sfa")
l.insert(3, "sda")
l.insert(2, "sdf")
l.insert(0, "sd")
l.printTable()
print(l.hashtable)





>>>>>>> f3fb868679a5a049df4840a35ab0c3098bf0648f
