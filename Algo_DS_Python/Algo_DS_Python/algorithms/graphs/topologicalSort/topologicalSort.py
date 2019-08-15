#Only for use in Python 2.6.0a2 and later
from __future__ import print_function
import sys
import os
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(".")
sys.path.append(dirpath + "/../")
sys.path.append(dirpath + '/../../../data_structures/')

from stacks.stacks import ArrayStack
from common import dag,V

def topologicalSort(V, adj):
    visited = {}
    stack = ArrayStack()
    sortedVertices = []
    for v in V:
        visited[v] = False

    for v in V:
        if visited[v] == False:
            topologicalSortUtil(v, visited, stack, adj)

    while stack.isEmpty() == False:
        temp = stack.pop()
        sortedVertices.append(temp)
        print(str(temp), end= " ")

    return sortedVertices

def topologicalSortUtil(v, visited, stack, adj):
    visited[v] = True
    for i in adj[v]:
        if visited[i] == False:
            topologicalSortUtil(i, visited, stack, adj)

    stack.push(v)

    
topologicalSort(V, dag)
    
