#Only for use in Python 2.6.0a2 and later
from __future__ import print_function

import sys
sys.path.append("../../../data_structures/linkedList")
sys.path.append("../../../data_structures/queues")
from queues import linkedListQueue

def BFS(s, adj):
    seen = {s: 0}
    parent = {s: None}
    count = 1
    queue = linkedListQueue()
    queue.enqueue(s)
    while not queue.isEmpty():
        n = queue.dequeue().data
        for v in adj[n]:
            if v not in seen:
                seen[v] = count
                parent[v] = n
                queue.enqueue(v)
        count += 1
    return seen

adj = {'s': set(['a', 'x']),
         'a': set(['s', 'z']),
         'x': set(['s', 'd', 'c']),
         'z': set(['a']),
         'd': set(['x', 'c', 'f']),
         'c': set(['x', 'd', 'f', 'v']),
         'f': set(['d', 'c', 'v']),
         'v': set(['c', 'f'])}

print(BFS('s', adj))

