#!/usr/bin/python3

import sys
import heapq
import itertools

class PriorityQueue:

    def __init__(self):
        self.pq = list()
        self.entry_finder = dict()
        self.counter = itertools.count()
        self.REMOVED = '<removed-task>'

    def add(self, task, priority):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder: self.remove(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

    def empty(self):
        return len(self.entry_finder) == 0

class AStar:
    def __init__(self, n, adj, cost, x, y):
        self.n = n                                 # Number of nodes
        self.inf = n*10**6                         # All distances in the graph are smaller
        self.gScore = [[self.inf]*n, [self.inf]*n] # Initialize distances for forward and backward searches
        self.fScore = [[self.inf]*n, [self.inf]*n]
        self.workset = []                          # All the nodes visited by forward or backward search
        self.G = adj
        self.W = cost
        self.x = x
        self.y = y

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        for v in self.workset:
            self.gScore[0][v], self.gScore[1][v] = self.inf, self.inf
            self.fScore[0][v], self.fScore[1][v] = self.inf, self.inf
        del self.workset[0:len(self.workset)]

    def distance(self, p1, p2):
        x1, x2 = self.x[p1], self.x[p2]
        y1, y2 = self.y[p1], self.y[p2]
        return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

    def relax(self, pq, side, u, i, p):
        v = self.G[side][u][i]
        if self.gScore[side][v] > self.gScore[side][u] + self.W[side][u][i]:
            self.gScore[side][v] = self.gScore[side][u] + self.W[side][u][i]
            guess = self.distance(p, v)
            self.fScore[side][v] = self.gScore[side][v] + guess
            pq[side].add(v, self.fScore[side][v])
            self.workset.append(v)

    def process(self, pq, side, u, p):
        for i in range(len(self.G[side][u])):
            self.relax(pq, side, u, i, p)

    def query(self, s, t):
        self.clear()
        guess = self.distance(s, t)
        self.fScore[0][s], self.fScore[1][t] = guess, guess
        self.gScore[0][s], self.gScore[1][t] = 0, 0
        pq = [PriorityQueue(), PriorityQueue()]
        proc = [[], []]
        pq[0].add(s, self.fScore[0][s]), pq[1].add(t, self.fScore[1][t])
        while not pq[0].empty() and not pq[1].empty():
            v = pq[0].pop()
            self.process(pq, 0, v, t)
            proc[0].append(v)
            self.workset.append(v)
            if v in proc[1]: return self.shortest_path(s, t, proc)

            v = pq[1].pop()
            self.process(pq, 1, v, s)
            proc[1].append(v)
            self.workset.append(v)
            if v in proc[0]: return self.shortest_path(s, t, proc)
        return -1

    def shortest_path(self, s, t, proc):
        distance = self.inf
        for v in proc[0] + proc[1]:
            if self.gScore[0][v] + self.gScore[1][v] < distance:
                distance = self.gScore[0][v] + self.gScore[1][v]
        return distance

def readl():
    return map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    n,m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u, v, c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        print(astar.query(s-1, t-1))