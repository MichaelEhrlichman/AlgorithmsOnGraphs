#Uses python3

import sys

sys.setrecursionlimit(200000)

def explore(adj,v,component_list,component_number):
    component_list[v] = component_number
    for w in adj[v]:
        if component_list[w] == 0:
            explore(adj,w,component_list,component_number)

def dfs(adj,v,visited,pre,post,tic):
    visited[v] = True
    tic[0] += 1
    pre[v] = tic[0]
    for w in adj[v]:
        if not visited[w]:
            dfs(adj,w,visited,pre,post,tic)
    tic[0] += 1
    post[v] = tic[0]

def toposort(adj):
    tic = [0]
    visited = [False for i in range(len(adj))]
    pre = [-1 for i in range(len(adj))]
    post = [-1 for i in range(len(adj))]
    for v in range(len(adj)):
        if visited[v] == False:
            dfs(adj,v,visited,pre,post,tic)
    order = list(range(len(post)))
    return sorted(order,key=lambda x: post[x],reverse=True)

def number_of_strongly_connected_components(adj,adr):
    rpost_order = toposort(adr)
    component_list = [0 for i in range(len(adr))]
    component_number = 0
    for v in rpost_order:
        if component_list[v] == 0:
            component_number += 1
            explore(adj,v,component_list,component_number) 
    return component_number

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adr = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adr[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj,adr))
