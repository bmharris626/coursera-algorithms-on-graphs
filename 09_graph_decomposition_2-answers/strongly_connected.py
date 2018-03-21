#Uses python3

import sys

sys.setrecursionlimit(200000)

class directedGraph:

    def __init__(self, G):
        self.G = G
        self.n = len(G)

    def transpose(self):
        G_t = [list() for i in range(self.n)]
        for v in range(self.n):
            for u in self.G[v]:
                G_t[u].append(v)
        return G_t

    def explore(self, v, visited):
        self.clock += 1
        self.pre[v] = self.clock
        visited[v] = True
        for u in self.G[v]:
            if not visited[u]:
                self.predecessor[u] = v
                self.explore(u, visited)
        self.clock += 1
        self.post[v] = self.clock
        self.topsort.insert(0, v)

    def dfs(self):
        visited, self.predecessor = list(), list()
        self.topsort = list()
        for v in range(self.n):
            visited.append(False)
            self.predecessor.append(None)
        self.pre = self.predecessor.copy()
        self.post = self.predecessor.copy()
        self.clock = 0
        for v in range(self.n):
            if not visited[v]: self.explore(v, visited)

def number_of_strongly_connected_components(adj):
    graph = directedGraph(adj)
    graph.dfs()
    adj_t = graph.transpose()
    graph_t = directedGraph(adj_t)
    visited, graph_t.predecessor = list(), list()
    graph_t.topsort = list()
    for v in range(graph_t.n):
        visited.append(False)
        graph_t.predecessor.append(None)
    graph_t.pre = graph_t.predecessor.copy()
    graph_t.post = graph_t.predecessor.copy()
    graph_t.clock, scc = 0, 0
    for v in graph.topsort:
        if not visited[v]: 
            graph_t.explore(v, visited)
            scc += 1
    return scc

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
