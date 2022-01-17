#Uses python3
import sys
import math

class Set():
    def __init__(self,x,y):
        self.parent = [i for i in range(len(x))]
        self.rank = [0 for i in range(len(x))]
        self.x = x
        self.y = y
        self.d = self.makeEdges(x,y)

    def makeEdges(self,x,y):
        dists = [[None for j in range(len(x))] for i in range(len(x))]
        for ji, xi,yi in enumerate(zip(x,y)):
            for jf, xf,yf in enumerate(zip(x,y)):
                if ji != jf:
                    self.d[ji][jf] = ( (xi-xf)^2 + (yi-yf)^2 )^0.5
                else:
                    self.d[ji][jf] = float('inf')

    def union(i_id,j_id):
        if rank[i_id] > rank[j_id]:
            parent[j_id] = i_id
        else:
            parent[i_id] = j_id
            if rank[i_id] == rank[j_id]:
                rank[j_id] += 1
        

def clustering(x, y, k):
    mySet = Set(x,y)
    
    return -1.


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
