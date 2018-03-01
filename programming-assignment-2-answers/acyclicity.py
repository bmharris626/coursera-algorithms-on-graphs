#Uses python3

import sys

class directedGraph:

    def __init__(self, G):
        self.G = G

    def explore(self, v):
        self.visited[v] = True
        self.preVisit(v)
        for w in self.G[v]:
            if not self.visited[v]: self.explore(v)
        self.postVisit(v)

    def dfs(self):
        self.visited = [False for i in range(len(self.G))]
        self.clock = 0
        self.pre = self.visited.copy()
        self.post = self.visited.copy()
        for i in range(len(self.G)):
            if not self.visited[i]: self.explore(i)

    def preVisit(self, v):
        self.pre[v] = self.clock
        self.clock += 1

    def postVisit(self, v):
        self.post[v] = self.clock
        self.clock += 1

    def topologicalSort(self):
        self.dfs()
        A = list(zip(range(len(self.G)), self.pre, self.post))
        return sorted(A, key=lambda x: x[2], reverse=True)

def acyclic(adj):
    graph = directedGraph(adj)
    G = graph.topologicalSort()
    print(G)
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
    print(acyclic(adj))
