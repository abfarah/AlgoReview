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

    def printTree(self):
        if self.tree == None:
            print("Tree is empty")
            return None
        else:
            self.printWRecursive(self.tree)

    def printWRecursive(self, tree):
        if tree != None:
            self.printWRecursive(tree.left)
            print(tree.val)
            self.printWRecursive(tree.right)

    def findMin(self):
        if self.tree == None:
            print("Tree is empty")
        else:
            return self.findMinWRecursion(self.tree)


    def findMinWRecursion(self, tree):
        if tree.left == None:
            return tree.val
        else:
            return self.findMinWRecursion(tree.left)

    def findMax(self):
        if self.tree == None:
            print("Tree is empty")
        else:
            return self.findMaxWRecursion(self.tree)

    def findMaxWRecursion(self, tree):
        if tree.right == None:
            return tree.val
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

        if leftHeight <= rightHeight:
            return rightHeight +1
        else:
            return leftHeight +1


