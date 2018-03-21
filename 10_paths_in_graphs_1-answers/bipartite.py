#Uses python3

import sys
import queue

class undirectedGraph:

    def __init__(self, G):
        self.G = G
        self.n = len(G)

    def bfs(self, S):
        dist = [-1 for u in self.G]
        dist[S] = 0
        Q = queue.Queue()
        Q.put(S)
        while not Q.empty():
            u = Q.get()
            for v in self.G[u]:
                if dist[v] == -1: 
                    Q.put(v)
                    dist[v] = dist[u] + 1
        return dist

    def is_bipartite(self):
        parts = [-1 for u in self.G]
        for u in range(self.n):
            if parts[u] == -1: parts[u] = 1
            if parts[u] == 1: p = 2
            else: p = 1
            for v in self.G[u]:
                if parts[v] == -1: parts[v] = p
                if parts[v] != p: return False
        return True

def bipartite(adj):
    graph = undirectedGraph(adj)
    if graph.is_bipartite(): return 1
    return 0

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
    print(bipartite(adj))
