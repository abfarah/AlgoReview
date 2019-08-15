#Only for use in Python 2.6.0a2 and later
from __future__ import print_function

import sys
import os
dirpath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(".")
sys.path.append("/../")
sys.path.append(dirpath + "/../../../data_structures/")
from queues.queues  import linkedListQueue
from common import adj

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

print(BFS('s', adj))

