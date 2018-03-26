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
        if task in self.entry_finder:
            self.remove(task)
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

    def top(self):
        if len(self.pq) == 0: return 0
        priority, count, task = self.pq[0]
        while len(self.pq) > 0 and task == self.REMOVED:
            task = self.pop()
            if len(self.pq) == 0: return 0
            priority, count, task = self.pq[0]
        priority, count, task = self.pq[0]
        if task == None: return 0
        return priority

    def find(self, task):
        return self.entry_finder.get(task, None)

    def empty(self):
        return len(self.entry_finder) == 0

class BiDij:
    def __init__(self, n, adj, cost):
        self.n = n                              # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.p = [[None]*n, [None]*n]
        self.workset = []                       # All the nodes visited by forward or backward search
        self.G = adj
        self.W = cost

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        for v in self.workset:
            self.d[0][v], self.d[1][v] = self.inf, self.inf
            self.p[0][v], self.p[1][v] = None, None
        del self.workset[0:len(self.workset)]

    def relax(self, pq, side, u, i):
        v = self.G[side][u][i]
        if self.d[side][v] > self.d[side][u] + self.W[side][u][i]:
            self.d[side][v] = self.d[side][u] + self.W[side][u][i]
            self.p[side][v] = u
            pq[side].add(v, self.d[side][v])
        self.workset.append(v)

    def process(self, pq, side, u):
        for i in range(len(self.G[side][u])):
            self.relax(pq, side, u, i)

    def query(self, s, t):
        self.clear()
        if s == t: return 0
        self.d[0][s], self.d[1][t] = 0, 0
        pq = [PriorityQueue(), PriorityQueue()]
        pq[0].add(s, self.d[0][s]), pq[1].add(t, self.d[0][s])
        while not pq[0].empty() and not pq[1].empty():
            v = pq[0].pop()
            self.process(pq, 0, v)
            self.workset.append(v)
            if pq[1].find(v) != None: return self.shortest_path(s, t, pq)
            v = pq[1].pop()
            self.process(pq, 1, v)
            self.workset.append(v)
            if pq[0].find(v) != None: return self.shortest_path(s, t, pq)
        return -1

    def shortest_path(self, s, t, pq):
        distance, u_best = self.inf, None
        while not pq[0].empty():
            u = pq[0].pop()
            if self.d[0][u] + self.d[1][u] < distance:
                u_best = u
                distance = self.d[0][u] + self.d[1][u]
            if self.d[0][u] + pq[1].top() > distance: break 
        while not pq[0].empty():
            u = pq[0].pop()
            if self.d[0][u] + self.d[1][u] < distance:
                u_best = u
                distance = self.d[0][u] + self.d[1][u]
            if self.d[1][u] + pq[0].top() > distance: break 
        for key in pq[1].entry_finder:
            d, c, u = pq[1].entry_finder[key]
            if self.d[0][u] + self.d[1][u] < distance:
                u_best = u
                distance = self.d[0][u] + self.d[1][u]
        path, last = [], u_best
        while last != s:
            path.append(last)
            last = self.p[0][last]
        path = path[::-1]
        last = u_best
        while last != t:
            last = self.p[1][last]
            path.append(last)
        return distance

def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n, adj, cost)
    for i in range(t):
        s, t = readl()
        print(bidij.query(s-1, t-1))