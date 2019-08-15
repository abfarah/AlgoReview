from __future__ import print_function
import sys
import os
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append( '.' )
sys.path.append(dirpath + '/../' )

from queues.queues import linkedListQueue


class Node:
    def __init__(self, data=None):
        self.val = data
        self.right = None
        self.left = None

class BST:
    def __init__(self, data=None):
        self.tree = None if data is None else Node(data)

    def isEmpty(self):
        if self.tree == None:
            return True
        else:
            return False

    def insert(self, x):
        if self.tree != None:
            self.insertWRecursive(self.tree, x)
        else:
            self.tree = Node(x)

    def insertWRecursive(self, t, x):
        if x <= t.val:
            if(t.left == None):
                t.left = Node(x)
            else:
                self.insertWRecursive(t.left, x)
        else:
            if (t.right == None):
                t.right = Node(x)
            else:
                self.insertWRecursive(t.right, x)

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

    def height(self):
        if self.tree == None:
            print("Tree is empty")
        else:
            return self.findHeight(self.tree)

    def findHeight(self, tree):
        if tree == None:
            return 0
        leftHeight = self.findHeight(tree.left)
        rightHeight = self.findHeight(tree.right)

        if leftHeight > rightHeight:
            return leftHeight +1
        else:
            return rightHeight +1

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
            self.deleteUtil(self.tree, x)

    def deleteUtil(self, tree, x):
        if tree == None:
            return tree
        elif x < tree.val:
            tree.left = self.deleteUtil(tree.left, x)
        elif x > tree.val:
            tree.right = self.deleteUtil(tree.right, x)
        else:
            if tree.right == None and tree.left == None:
                return None
            elif tree.left == None and tree.right != None:
                return tree.right
            elif tree.right == None and tree.left != None:
                return tree.left
            else:
                temp = self.findMinWRecursion(tree.right)
                tree.val = temp.val
                tree.right = self.deleteUtil(tree.right, temp.val)
        return tree

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

