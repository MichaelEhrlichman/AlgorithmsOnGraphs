#Uses python3
import sys
import math

def findMin(cost):
    minimum = cost[0]
    minimum_i = 0
    for i in range(1,len(cost)):
        if cost[i] < minimum:
            minimum = cost[i]
            minimum_i = i
    return minimum_i

def update_and_delete(inew,x,y,cost):
    for i,(xf,yf) in enumerate(zip(x,y)):
        if i != inew:
            costnew = ( (x[inew]-xf)**2 + (y[inew]-yf)**2 )**0.5 
            if costnew < cost[i]:
                cost[i] = costnew
    del x[inew]
    del y[inew]
    del cost[inew]

def minimum_distance(x, y):
    #Prim's Algorithm using cost as the array-based priority queue
    #The graph is dense, every verted is connected to every other vertex, so O(V^2) wins over O(E log V)
    #All we are interested in for this problem is the total length of edges.
    cost = [float('inf') for i in range(len(x))]

    #Start with element 0
    result = 0
    cost[0] = 0
    inew = 0
    update_and_delete(0,x,y,cost)

    while x:
        inew = findMin(cost)
        result += cost[inew]
        update_and_delete(inew,x,y,cost)

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
