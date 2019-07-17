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
        if t == None:
            t = Node(x)
        elif x <= t.val:
            t.left = insertWRecursive(t.left, x)
        else:
            t.right = insertWRecursive(t.right, x)
        return t

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
            printTree(tree.left)
            print(tree.val)
            printTree(tree.right)
b = BST(6)
b.insert(7)
b.printTree()
b.insert(9)
b.printTree(b)


