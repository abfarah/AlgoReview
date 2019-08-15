#Only for use in Python 2.6.0a2 and later
from __future__ import print_function
import sys
import os
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append( '.' )
sys.path.append( dirpath + '/../' )

from linkedList.linkedList import LinkedList

class ArrayStack:
    def __init__(self, data=None):
        self.stack = [None] * 10 if data is None else [data] + [None] * 9
        self.size = 1 if data is not None else 0
        self.top = 0 if data is not None else -1

    def isEmpty(self):
        if self.top == -1:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.stack[self.top]
    
    def push(self, x):
        self.top += 1
        if self.top > len(self.stack)-1:
            self.resize()
        self.stack[self.top] = x
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        self.top -= 1
        self.size -= 1
        return self.stack[self.top+1]
    
    def printStack(self):
        print("Stack is:", end=" ")
        for i in range(self.size):
            print(self.stack[i], end=" ")
        print("")

    def resize(self):
        newArr = [None] * (len(self.stack)*2)
        for i in range(0, len(self.stack)):
            newArr[i] = self.stack[i]
        self.stack = newArr


class LinkedListStack:
    def __init__(self, data=None):
        self.stack = LinkedList(data)
        self.size = self.stack.size

    def isEmpty(self):
        if self.size <= 0:
            return True
        return False

    def peek(self):
        return self.stack.head.data

    def push(self, x):
        self.stack.insertHead(x)
        self.size += 1
        
    def pop(self):
        x = self.stack.head.data
        self.stack.deleteHead()
        return x

    def printStack(self):
        print("Stack", end="")
        self.stack.printList()


def checkBalancedParentheses(s):
    stack = ArrayStack()
    for i in s:
        if i == "(" or i == "{" or i == "[":
            stack.push(i)
        elif i == ")" or i == "}" or i =="]":
            if stack.isEmpty():
                return False
            x = stack.pop()
            if i == ")" and x != "(":
                return False
            if i == "}" and x != "{":
                return False
            if i == "]" and x != "]":
                return False

    if stack.isEmpty():
        return True
    else:
        return False

def evalPostfix(exp):
    s = LinkedListStack()
    for i in exp:
        if i == "*" or i == "/" or i == "+" or i == "-":
            op2 = s.pop()
            op1 = s.pop()
            res = 0;
            if i == "*":
                res = op1 * op2
            elif i == "/":
                res = op1 / op2
            elif i == "+":
                res = op1 + op2
            elif i == "-":
                res = op1 - op2
            s.push(res)
        else:
            s.push(int(i))
    return s.pop()

def evalPrefix(exp):
    s = LinkedListStack()
    for x in range(len(exp), 0, -1):
        i = exp[x - 1]
        if i == "*" or i == "/" or i == "+" or i == "-":
            op1 = s.pop()
            op2 = s.pop()
            res = 0;
            if i == "*":
                res = op1 * op2
            elif i == "/":
                res = op1 / op2
            elif i == "+":
                res = op1 + op2
            elif i == "-":
                res = op1 - op2
            s.push(res)
        else:
            s.push(int(i))
    return s.pop()

def infixToPostfix(exp):
    s = ArrayStack()
    res = []
    for i in exp:
        print("i is: ", end="")
        print(i)
        if i == "*" or i == "/" or i == "+" or i == "-":
            while s.isEmpty() == False and s.peek() != "(" and getPrecedence(s.peek(), i) == s.peek():
                res.append(s.pop())
                print("appended ", end=" ")
                print(i)
            s.push(i)
            print("pushed: ", end="")
            print(i)
        elif i == "(":
            s.push(i)
        elif i == ")":
            while s.isEmpty() == False and s.peek() != "(":
                res.append(s.pop())
            s.pop()
        else:
            res.append(i)
    while s.isEmpty() == False:
        res.append(s.pop())
        print("Whileloop after case")
    arr = "".join(res)
    return arr       

def getPrecedence(x, y):
    if x == y:
        return x
    elif x == "*" or x == "/" and y == "+" or y == "-":
        return x
    else:
        return y
