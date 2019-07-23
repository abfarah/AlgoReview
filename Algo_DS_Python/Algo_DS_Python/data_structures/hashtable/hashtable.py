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

class HashWChaining:
    def __init__(self):
        self.bucket = None

    def hashItem(self,x):
        h = (randrange(0,x-1)*x + randrange(0,x-1)) % 107923
        return h

    def get(self, key):
        h = self.hashItem(key)
        return self.bucket[key]

z = HashWChaining()
print(z.hashItem(6))
print(z.hashItem(6))

