#Only for use in Python 2.6.0a2 and later
from __future__ import print_function
import sys
import os
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(".")
sys.path.append(dirpath + "/../")

from common import adj,V

def DFS_Visit(s, adj, parent):
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_Visit(v, adj, parent)

def DFS(V, adj):
    parent = {}
    for v in V:
        if v not in parent:
            parent[v] = None
            DFS_Visit(v, adj, parent)
    return parent

print(DFS(V, adj))










