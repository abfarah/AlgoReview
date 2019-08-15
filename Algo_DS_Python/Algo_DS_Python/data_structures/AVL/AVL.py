from __future__ import print_function
import sys
import os
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append( '.' )
sys.path.append(dirpath + '/../' )

from queues.queues import linkedListQueue

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

    def isEmpty(self):
        if self.tree == None:
            return True
        else:
            return False

    def getBalance(self, x):
        if x == None:
            return 0
        else:
            return self.getHeight(x.left) - self.getHeight(x.right)

    def insert(self, x):
        if self.tree == None:
            print("Tree is empty")
        else:
            self.tree = self.insertUtil(self.tree, x)
            return self.tree

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
        t.height = max(self.getHeight(t.left), self.getHeight(t.right)) + 1
        b = self.getBalance(t)
        if b > 1 and x < t.left.val:
            return self.rightRotate(t)
        if b < -1 and x > t.right.val:
            return self.leftRotate(t)
        if b > 1 and x > t.left.val:
            t.left = self.leftRotate(t.left)
            return self.rightRotate(t)
        if b < -1 and x < t.right.val:
            t.right = self.rightRotate(t.right)
            return self.leftRotate(t)
        return t

    def leftRotate(self, x):
        i = x.right
        j = i.left
        i.left = x
        x.right = j
        x.height = max(self.getHeight(x.left), self.getHeight(x.right)) + 1
        i.height = max(self.getHeight(i.left), self.getHeight(i.right)) + 1
        return i

    def rightRotate(self, x):
        i = x.left
        j = i.right
        i.right = x
        x.left = j
        x.height = max(self.getHeight(x.left), self.getHeight(x.right)) + 1
        i.height = max(self.getHeight(i.left), self.getHeight(i.right)) + 1
        return i

    def find(self, x):
        temp = self.tree
        while temp != None:
            if temp.val == x:
                return temp
            else:
                temp = temp.left if temp.val > x else temp.right
        print("No value " + str(x) + " in binary search tree")
        return None

    def printTree(self):
        return self.inorder()

    def findMin(self):
        if self.tree == None:
            print("Tree is empty")
        else:
            return self.findMinWRecursion(self.tree)

    def findMinWRecursion(self, tree):
        if tree.left == None:
            return tree
        else:
            return self.findMinWRecursion(tree.left)

    def findMax(self):
        if self.tree == None:
            print("Tree is empty")
        else:
            return self.findMaxWRecursion(self.tree)

    def findMaxWRecursion(self, tree):
        if tree.right == None:
            return tree
        else:
            return self.findMaxWRecursion(tree.right)

    def getHeight(self, x):
        if x == None:
            return -1
        else:
            return x.height

    def isBinarySearchTree(self, tree=None):
        INT_MAX = sys.maxsize
        INT_MIN = -sys.maxsize-1
        if tree == None:
            tree = self.tree
        if tree == None:
            print("Tree is empty")
        else:
            return self.isBstUtil(tree, INT_MIN, INT_MAX)

    def isBstUtil(self, tree, intMin, intMax):
        if tree == None:
            return True
        if tree.val >= intMin and tree.val <= intMax and self.isBstUtil(tree.left, intMin, tree.val) and self.isBstUtil(tree.right, tree.val, intMax):
            return True
        else:
            return False

    def delete(self, x):
        if self.tree == None:
            print("Tree is empty")
        else:
            self.tree = self.deleteUtil(self.tree, x)
            return self.tree

    def deleteUtil(self, t, x):
        if t == None:
            return t
        elif x < t.val:
            t.left = self.deleteUtil(t.left, x)
        elif x > t.val:
            t.right = self.deleteUtil(t.right, x)
        else:
            if t.right == None and t.left == None:
                return None
            elif t.left == None and t.right != None:
                return tree.right
            elif t.right == None and t.left != None:
                return t.left
            else:
                temp = self.findMinWRecursion(t.right)
                t.val = temp.val
                t.right = self.deleteUtil(t.right, temp.val)
        if t == None:
            return tree
        t.height = max(self.getHeight(t.left), self.getHeight(t.right)) + 1
        b = self.getBalance(t)
        if b > 1 and self.getBalance(t.left) >= 0:
            return self.rightRotate(t)
        if b < -1 and self.getBalance(t.left) <= 0:
            return self.leftRotate(t)
        if b > 1 and self.getBalance(t.left) < 0:
            t.left = self.leftRotate(t.left)
            return self.rightRotate(t)
        if b < -1 and self.getBalance(t.left) > 0:
            t.right = self.rightRotate(t.right)
            return self.leftRotate(t)
        return t

    def getSuccessor(self, x):
        if self.tree == None:
            print("Tree is empty")
        else:
            current = self.find(x)
            if current == None:
                return None
            if current.right != None:
                return self.findMinWRecursion(current.right)
            else:
                successor = None
                ancestor = self.tree
                while ancestor != current:
                    if current.val < ancestor.val:
                        successor = ancestor
                        ancestor = ancestor.left
                    else:
                        ancestor = ancestor.right
                return successor

    def preorder(self):
        if self.tree == None:
            print("Tree is empty")
        else:
            result =  self.preorderWRecursion(self.tree)
            print("")
            return result

    def preorderWRecursion(self, tree):
        if tree != None:
            print(tree.val, end=" ")
            self.preorderWRecursion(tree.left)
            self.preorderWRecursion(tree.right)


    def postorder(self):
        if self.tree == None:
            print("Tree is empty")
        else:
            result =  self.postorderWRecursion(self.tree)
            print("")
            return result


    def postorderWRecursion(self, tree):
        if tree != None:
            self.postorderWRecursion(tree.left)
            self.postorderWRecursion(tree.right)
            print(tree.val, end=" ")


    def inorder(self):
        if self.tree == None:
            print("Tree is empty")
        else:
            result = self.inorderWRecursion(self.tree)
            print("")
            return result

    def inorderWRecursion(self, tree):
        if tree != None:
            self.inorderWRecursion(tree.left)
            print(tree.val, end=" ")
            self.inorderWRecursion(tree.right)

    def levelOrder(self):
        if self.tree == None:
            print("Tree is empty")
        else:
            queue = linkedListQueue()
            queue.enqueue(self.tree)
            print("BST in level order : ", end="")
            while not queue.isEmpty():
                temp = queue.dequeue()
                print(temp.data.val, end=" ")
                if temp.data.left != None:
                    queue.enqueue(temp.data.left)
                if temp.data.right != None:
                    queue.enqueue(temp.data.right)
        print("")

