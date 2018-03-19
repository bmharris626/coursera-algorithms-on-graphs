#Uses python3

import sys
import heapq

class DirectedGraph:

    def __init__(self, G, C):
        self.n = len(G)
        self.G = G
        self.W = C

    def dijkstra(self, s):
        dist, prev, H = list(), list(), list()
        for i in range(self.n):
            dist.append(float('inf'))
            prev.append(None)
        heapq.heappush(H, (0, s))
        dist[s] = 0
        while len(H) > 0:
            u = heapq.heappop(H)[1]
            for i in range(len(self.G[u])):
                v = self.G[u][i]
                if dist[v] > dist[u] + self.W[u][i]:
                    dist[v] = dist[u] + self.W[u][i]
                    prev[v] = u
                    heapq.heappush(H, (dist[v], v))
        return dist

def distance(adj, cost, s, t):
    graph = DirectedGraph(adj, cost)
    dist = graph.dijkstra(s)
    if dist[t] == float('inf'): return -1
    return dist[t]

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
