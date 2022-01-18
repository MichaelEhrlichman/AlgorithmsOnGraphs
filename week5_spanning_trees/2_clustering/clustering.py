#Uses python3
import sys

class Set():
    def __init__(self,x,y):
        self.n = len(x)
        self.parent = [i for i in range(self.n)]
        self.ndisjoint = self.n
        self.rank = [0 for i in range(self.n)]
        self.x = x
        self.y = y
        self.d = self.makeEdges(x,y)
        self.d.sort(key=lambda x:x[2])

    def makeEdges(self,x,y):
        dists = [None for i in range(len(x)**2)]
        i = 0
        for ji,(xi,yi) in enumerate(zip(x,y)):
            for jf,(xf,yf) in enumerate(zip(x,y)):
                if ji != jf:
                    dists[i] = [ji,jf,( (xi-xf)**2 + (yi-yf)**2 )**0.5]
                else:
                    dists[i] = [ji,jf,float('inf')]
                i += 1
        return dists

    def Find(self,i):
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def Union(self,i,j):
        i_id = self.Find(i)
        j_id = self.Find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1
        self.ndisjoint -= 1
        

def clustering(x, y, k):
    # Adapt Kruskal's algorithm
    mySet = Set(x,y)
    for ix,iy,d in mySet.d:
        if mySet.ndisjoint == k-1:
            break
        mySet.Union(ix,iy)
    #print(mySet.d)
    #print(mySet.parent,mySet.ndisjoint,d)
    return d


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
