#Uses python3

import sys

def negative_cycle(adj, cost):
    m = len(adj)
    dist = [1000 for i in range(m)]
    prev = [None for i in range(m)]
    for i in range(m):  #BellmanFord with negative cycle detection
        relax_happened = 0
        for u,vclst in enumerate(zip(adj,cost)):
            vlst = vclst[0]
            clst = vclst[1]
            for v,c in zip(vlst,clst):
                #relax(u,v)
                if dist[v] > dist[u] + c:
                    relax_happened = 1
                    dist[v] = dist[u] + c
                    prev[v] = u
        if not relax_happened:
            return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
