#Uses python3
import sys
import heapq

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)

def find(sets, p):
    for i in range(len(sets)):
        if p in sets[i]: return i

def build_heap(x, y):
    n = len(x)
    h = list()
    for i in range(n):
        p1 = (x[i], y[i])
        for j in range(n-i-1):
            p2 = (x[i+j], y[i+j])
            d = distance(p1, p2)
            heapq.heappush(h, (d, p1, p2))
    return h

def minimum_distance(x, y):
    result = 0.
    sets = [{(x[i], y[i])} for i in range(n)]
    h = build_heap(x, y)
    for i in range(len(h)):
        d, u, v = heapq.heappop(h)
        uSet, vSet = find(sets, u), find(sets, v)
        if uSet != vSet:
            u, v = sets.pop(uSet), sets.pop(vSet)
            s = u | v
            sets.append(s)
            result += d
    return result

"""
TRY IMPLEMENTING NOT KRUSKAL
""" 

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

"""
4
0 0
0 1
1 0
1 1
"""