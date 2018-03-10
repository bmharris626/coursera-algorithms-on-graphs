#Uses python3

import sys
import queue

class undirectedGraph:

    def __init__(self, G):
        self.G = G

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


def distance(adj, s, t):
    graph = undirectedGraph(adj)
    dist = graph.bfs(s)
    return dist[t]

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
