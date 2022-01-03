#Uses python3

import sys

def explore(adj,v,component_list,component_number):
    component_list[v] = component_number
    for w in adj[v]:
        if component_list[w] == 0:
            explore(adj,w,component_list,component_number)

def number_of_components(adj):
    component_list = [0 for i in range(len(adj))]
    component_number = 0
    for v in range(len(adj)):
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
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
