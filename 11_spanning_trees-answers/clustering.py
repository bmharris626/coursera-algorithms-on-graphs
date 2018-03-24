#Uses python3
import sys
import math
import heapq

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)

def find(pi, v):
    while v != pi[v]:
        v = find(pi, pi[v])
    return v

def merge(pi, rank, x, y, d):
    r_x = find(pi, x)
    r_y = find(pi, y)
    if r_x == r_y: return
    if rank[r_x] > rank[r_y]:
        pi[r_y] = r_x
    else:
        pi[r_x] = r_y
        if rank[r_x] == rank[r_y]: rank[r_y] += 1

def clustering(x, y, k):
    n = len(x)
    h, pi, rank, gamma = [], [], [], 0
    c = 0
    for i in range(n):
        pi.append(i)
        rank.append(0)
        p1 = (x[i], y[i])
        for j in range(n-1-i):
            p2 = (x[1+i+j], y[1+i+j])
            heapq.heappush(h, [distance(p1, p2), c, i, 1+i+j])
            c += 1
    while (len(h) > 0) and (n >= k):
        d, c, u, v = heapq.heappop(h)
        if find(pi, u) != find(pi, v):
            merge(pi, rank, u, v, d)
            if d > gamma: gamma = d
            n -= 1
    return float(gamma)


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