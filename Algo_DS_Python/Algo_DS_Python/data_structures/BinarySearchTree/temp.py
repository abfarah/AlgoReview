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
        if t.val < x:
            if t.right == None:
                t.right = Node(x)
            else:
                self.insertWRecursive(t.right, x)
        else:
            if t.left == None:
                t.left = Node(x)
            else:
                self.insertWRecursive(t.left, x)

    def find(self, x):
        temp = self.tree
        while temp != None:
            if temp.val == x:
                return temp
            else:
                temp = temp.left if temp.val > x else temp.right
        return None

    def printTree(self, tree):
        if tree == None:
            print("Tree is empty")
        else:
            self.printTree(tree.left)
            print(tree.val)
            self.printTree(tree.right)
b = BST(6)
b.insert(7)
b.printTree(b)
b.insert(9)
b.printTree(b)


