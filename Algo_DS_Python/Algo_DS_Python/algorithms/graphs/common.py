adj = {'s': set(['a', 'x']),
        'a': set(['s', 'z']),
        'x': set(['s', 'd', 'c']),
        'z': set(['a']),
        'd': set(['x', 'c', 'f']),
        'c': set(['x', 'd', 'f', 'v']),
        'f': set(['d', 'c', 'v']),
        'v': set(['c', 'f'])}

V = ['s', 'a', 'x', 'z', 'd', 'c', 'f', 'v']

dag = {'s': set(['a', 'x']),
        'a': set(['z']),
        'x': set(['d', 'c']),
        'z': set([]),
        'd': set(['c', 'f']),
        'c': set(['f', 'v']),
        'f': set(['v']),
        'v': set([])}


