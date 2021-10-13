#Only for use in Python 2.6.0a2 and later
from __future__ import print_function

class Node:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()

    def letterPosition(self, l):
        return ord(l.lower()) - ord('a')

    def insert(self, word):
        word = word.lower()
        n = len(word)
        temp = self.root
        for i in range(n):
            index = self.letterPosition(word[i])
            if temp.children[index] == None:
                temp.children[index] = Node()
            temp = temp.children[index]
        temp.isEnd = True

    def search(self, word):
        word = word.lower()
        n = len(word)
        temp = self.root
        for i in range(n):
            index = self.letterPosition(word[i])
            if temp.children[index] == None:
                print("Nothing Found")
                return False
            temp = temp.children[index]
        if temp.isEnd == True:
            print("word Found")
            return True
        else:
            print("Nothing Found")
            return False

