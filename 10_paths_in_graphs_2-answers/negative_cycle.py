#Uses python3

import sys
import queue

class DirectedGraph:

    def __init__(self, G, C):
        self.n = len(G)
        self.G = G
        self.W = C

    def BellmanFord(self, s):
        dist, prev = list(), list()
        for i in range(self.n):
            dist.append(float('inf'))
            prev.append(None)
        dist[s] = 0
        for u in range(self.n-1):
            for i in range(len(self.G[u])):
                v = self.G[u][i]
                if dist[v] > dist[u] + self.W[u][i]:
                    dist[v] = dist[u] + self.W[u][i]
                    prev[v] = u
        return dist, prev

"""
6 11
1 6 -10
1 2 3
2 6 8
2 3 3
2 5 -5
3 5 1
3 6 3
3 4 2
5 4 0
6 5 5
6 2 2
"""

def is_negative_cycle(G, W, distance):
    for u in range(len(G)):
        for i in range(len(G[u])):
            v = G[u][i]
            if distance[v] > distance[u] + W[u][i]: return True
    return False

def negative_cycle(adj, cost):
    graph = DirectedGraph(adj, cost)
    Q = queue.Queue()
    Q.put(0)
    while not Q.empty():
        s = Q.get()
        distance, prev = graph.BellmanFord(s)
        if is_negative_cycle(adj, cost, distance): return 1
        for i in range(len(distance)):
            if distance[i] == float('inf'):
                Q.put(i)
                break
    return 0

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
    print(negative_cycle(adj, cost))
