#Uses python3

import sys

class directedGraph:

    def __init__(self, G):
        self.G = G

    def explore(self, v):
        self.visited[v] = True
        self.preVisit(v)
        for u in self.G[v]:
            if not self.visited[u]:
                self.predecessor[u] = v
                self.explore(u)
            if self.post[u] == None: self.cycles += 1
        self.postVisit(v)

    def dfs(self):
        self.visited, self.pre = list(), list()
        self.post, self.predecessor = list(), list()
        self.topsort = list()
        self.cycles = 0
        for i in range(len(self.G)):
            self.visited.append(False)
            self.pre.append(None)
            self.post.append(None)
            self.predecessor.append(None)
        self.clock = 0
        for i in range(len(self.G)):
            if not self.visited[i]: self.explore(i)

    def preVisit(self, v):
        self.pre[v] = self.clock
        self.clock += 1

    def postVisit(self, v):
        self.post[v] = self.clock
        self.topsort.append(v)
        self.clock += 1

def toposort(adj):
    graph = directedGraph(adj)
    graph.dfs()
    return reversed(graph.topsort)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

