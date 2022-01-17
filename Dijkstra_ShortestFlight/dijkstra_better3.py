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
        self.pos = list(range(self.n))
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
            pos_ix = self.data[i][1]
            par_pos_ix = self.data[self.parent(i)][1]
            self.pos[pos_ix], self.pos[par_pos_ix] = self.pos[par_pos_ix], self.pos[pos_ix]
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def sift_down(self,i):  # min-heap sift down
        minix = i
        lix = self.left_child(i)
        if lix <= self.n-1 and self.data[lix][0] < self.data[minix][0]:
            minix = lix
        rix = self.right_child(i)
        if rix <= self.n-1 and self.data[rix][0] < self.data[minix][0]:
            minix = rix
        if i != minix:
            pos_ix = self.data[i][1]
            sink_pos_ix = self.data[minix][1]
            self.pos[pos_ix], self.pos[sink_pos_ix] = self.pos[sink_pos_ix], self.pos[pos_ix]
            self.data[i], self.data[minix] = self.data[minix], self.data[i]
            self.sift_down(minix)

    def change_distance(self,v,d):
        i = self.pos[v]   #get location of node v in the heap data
        oldd = self.data[i][0]
        self.data[i][0] = d
        if d < oldd:
            self.sift_up(i)
        else:
            self.sift_down(i)

    def extract_min(self):
        dist,u = self.data[0]
        self.pos[u] = -1
        if self.n > 1:
            self.pos[self.data[-1][1]] = 0
            self.data[0] = self.data.pop()
            self.n -= 1
            self.sift_down(0)
        else:
            self.pos[0] = -1
            self.data.pop()
        return dist,u

    def insert(self,i,d):
        self.data.append([d,i])
        self.n += 1
        self.sift_up(self.n-1)

def distance(adj, cost, s, t):
    dist = [float('inf') for i in range(len(adj))]
    prev = [None for i in range(len(adj))]
    dist[s] = 0
    H = MinHeap(dist)
    while len(H.data) > 0:
        distu, u = H.extract_min() 
        #print(distu,u)
        for v,w in zip(adj[u],cost[u]):
            if dist[v] > distu + w:
                dist[v] = distu + w
                prev[v] = u
                H.change_distance(v,dist[v])  #Need to search heap for vertex v
                #print('   ',v,dist[v])
                #H.insert(v,dist[v])  #Need to search heap for vertex v
    return dist[t] if dist[t] < float('inf') else -1

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
