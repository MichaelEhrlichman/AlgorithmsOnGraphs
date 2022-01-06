#Uses python3

import sys

def explore(adj,v,visited,pre,post,tic):
    visited[v] = True
    tic[0] += 1
    pre[v] = tic[0]
    for w in adj[v]:
        if not visited[w]:
            explore(adj,w,visited,pre,post,tic)
    tic[0] += 1
    post[v] = tic[0]

def acyclic(adj):
    tic = [0]
    visited = [False for i in range(len(adj))]
    pre = [-1 for i in range(len(adj))]
    post = [-1 for i in range(len(adj))]
    for v in range(len(adj)):
        if visited[v] == False:
            explore(adj,v,visited,pre,post,tic)
    for v in range(len(adj)):
        for w in adj[v]:
            if post[v] < post[w]:
                return 1
    #print(pre)
    #print(post)
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
