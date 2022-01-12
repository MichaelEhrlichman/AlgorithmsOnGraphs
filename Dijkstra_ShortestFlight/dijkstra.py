#Uses python3

import sys
import queue

class MinHeap():
    ''' Min heap from my Data Structures course.
        Added extract_min to pop the top of the heap (the min).
        Added data type to heap to store vertex identifier for use in Dijkstra's algorithm.
    '''
    data = []
    n = 0

    def __init__(self,input_array):
        self.n = len(input_array)
        self.data = [list(a) for a in zip(input_array,range(self.n))]
        for i in range(self.n//2-1, -1, -1):
            self.sift_down(i)

    @staticmethod
    def parent(i):
        return (i-1)//2

    @staticmethod
    def left_child(i):
        return 2*i+1

    @staticmethod
    def right_child(i):
        return 2*i+2

    def sift_up(self,i):  #min-heap sift up
        while i > 0 and self.data[self.parent(i)][0] > self.data[i][0]:
            self.data[i], self.data[parent(i)] = self.data[parent(i)], self.data[i]
            i = parent(i)

    def sift_down(self,i):  # min-heap sift down
        minix = i
        lix = self.left_child(i)
        if lix <= self.n-1 and self.data[lix][0] < self.data[minix][0]:
            minix = lix
        rix = self.right_child(i)
        if rix <= self.n-1 and self.data[rix][0] < self.data[minix][0]:
            minix = rix
        if i != minix:
            self.data[i], self.data[minix] = self.data[minix], self.data[i]
            self.sift_down(minix)

    def change_distance(self,i,d):
        oldd,u = self.data[i]
        self.data[i][0] = d
        if d < oldd:
            self.sift_up(i)
        else:
            self.sift_down(i)
        #return u,oldd

    def extract_min(self):
        dist,u = self.data[0]
        self.data[0] = self.data.pop()
        self.sift_down(0)
        return dist,u

def distance(adj, cost, s, t):
    dist = [float('inf') for i in range(len(adj))]
    prev = [None for i in range(len(adj))]
    dist[s] = 0
    H = MinHeap(dist)
    while len(H) > 0:
        distu, u = H.extract_min() 
        for v in adj[u]:
            if dist[v] > distu
    return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
