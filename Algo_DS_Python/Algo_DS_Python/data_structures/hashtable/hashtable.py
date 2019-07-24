from __future__ import print_function
import sys
sys.path.append( '.' )
sys.path.append( '../linkedList' )

from linkedList import LinkedList
from random import randrange

class HashNode:
    def __init__(self, x, y):
        self.key = x
        self.value = y
        self.next = None

class HashWChaining:
    def __init__(self):
        self.hashtable = [[] for _ in range(10)]

    def hashItem(self,x):
        return x % len(self.hashtable)

    def get(self, key):
        h = self.hashItem(key)
        for i in self.hashtable[h]:
            if i.key == key:
                return i
        print("Can't be found")
        return None


    def insert(self, key, value):
        h = self.hashItem(key)
        i = HashNode(key, value)
        self.hashtable[h].append(i)

    def displayTable(self):
        count = 0
        for i in self.hashtable:
            print("")
            print(str(count))
            for j in i:
                if j != None:
                    print("Key is: " + str(j.key) + " and value is: " + str(j.value), end=" ")
            count+=1

