#Uses python3

import sys
import queue

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    m = len(adj)
    prev = [None for i in range(m)]
    distance[s] = 0
    reachable[s] = 1
    for i in range(len(shortest)):
        shortest[i] = 1
    for i in range(m):  #BellmanFord with negative cycle detection
        relax_happened = 0
        for u,vclst in enumerate(zip(adj,cost)):
            vlst = vclst[0]
            clst = vclst[1]
            for v,c in zip(vlst,clst):
                #relax(u,v)
                if reachable[u]:
                    reachable[v] = 1
                if distance[v] > distance[u] + c:
                    relax_happened = 1
                    distance[v] = distance[u] + c
                    prev[v] = u
                    if i == m-1:  #negative cycle detected
                        x = v
                        shortest[x] = 0
                        #flag all vertices of the negative cycle
                        for j in range(m):
                            x = prev[x]
                            shortest[x] = 0
                        #BFS to prune vertices reachable through the negative cycle
                        pruned = [False for i in range(m)]
                        Q = [v]
                        while Q:
                            u_ = Q.pop(0)
                            for v_ in adj[u_]:
                                if not pruned[v_]:
                                    Q.append(v_)
                                    pruned[v_] = True
                                    shortest[v_] = 0
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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
    #for x in range(n):
    #    if reachable[x] == 0:
    #        print(x+1,'*')
    #    elif shortest[x] == 0:
    #        print(x+1,'-')
    #    else:
    #        print(x+1,distance[x])

