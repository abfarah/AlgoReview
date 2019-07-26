#Only for use in Python 2.6.0a2 and later
from __future__ import print_function
parent = {}
def DFS_Visit(s, adj):
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            DFS_Visit(v, adj)

def DFS(V, adj):
    for v in V:
        if v not in parent:
            parent[v] = None
            DFS_Visit(v, adj)
    return parent

V = ['s', 'a', 'x', 'z', 'd', 'c', 'f', 'v']
adj = {'s': set(['a', 'x']),
         'a': set(['s', 'z']),
         'x': set(['s', 'd', 'c']),
         'z': set(['a']),
         'd': set(['x', 'c', 'f']),
         'c': set(['x', 'd', 'f', 'v']),
         'f': set(['d', 'c', 'v']),
         'v': set(['c', 'f'])}

print(DFS(V, adj))










