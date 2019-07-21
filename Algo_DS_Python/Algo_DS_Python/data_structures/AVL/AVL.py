from __future__ import print_function
import sys
sys.path.append( '.' )
sys.path.append( '../BinarySearchTree' )

from BST import BST

class AVLNode:
    def __init__(self, data=None):
        self.val = data
        self.right = None
        self.left = None
        self.parent = None
        self.height = 0

class AVL:
    def __init__(self, data=None):
        self.tree = None if data is None else AVLNode(data)

    def getHeight(self, x):
        if x == None:
            return -1
        else:
            return x.height

    def isEmpty(self):
        if self.tree == None:
            return True
        else:
            return False

    def updateHeight(self, x):
        if x == None:
            print("Tree is empty")
        else:
            l = self.getHeight(x.left)
            r = self.getHeight(x.right)
            x.height = max(l,r) +1

    def insert(self, x):
        if self.tree == None:
            print("Tree is empty")
        else:
            return self.insertUtil(self.tree, x)

    def insertUtil(self, t, x):
        if x <= t.val:
            if(t.left == None):
                t.left = AVLNode(x)
                t.left.parent = t
            else:
                self.insertUtil(t.left, x)
        else:
            if (t.right == None):
                t.right = AVLNode(x)
                t.right.parent = t
            else:
                self.insertUtil(t.right, x)

        self.updateHeight(t)
        # TODO: finish insert method, create helper rotation methods to maintain the AVL Tree invariant
        
        
a = AVL(6)

a.insert(4)
a.insert(7)
a.insert(2)
a.insert(5)
a.insert(8)
print(a.tree.height)
