#Uses python3

import sys
import queue

def bipartite(adj):
    part = [None for i in range(len(adj))]
    for s in range(len(adj)):
        if part[s] == None:
            #new component everytime we are here
            queue = []
            queue.append(s)
            part[s] = -1
            while queue:
                u = queue.pop(0)
                for v in adj[u]:
                    if part[v] == None:
                        part[v] = -part[u]
                        queue.append(v)
                    elif part[v] == part[u]:
                        return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
