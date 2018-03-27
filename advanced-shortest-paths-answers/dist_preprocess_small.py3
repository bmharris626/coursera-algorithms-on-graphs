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
        while pq[0][2] == self.REMOVED:
            task = self.pop()
            if len(self.pq) == 0: return 0
        priority, count, task = self.pq[0]
        return priority

    def find(self, task):
        return self.entry_finder.get(task, None)

    def empty(self):
        return len(self.entry_finder) == 0

class DistPreprocessSmall:
    def __init__(self, n, adj, cost):
        # See description of these parameters in the starter for friend_suggestion
        self.n = n
        self.INFINITY = n * maxlen
        self.G, self.W = adj, cost
        self.bidistance = [[self.INFINITY] * n, [self.INFINITY] * n]
        self.visited = [False] * n
        self.visited = []
        self.q = PriorityQueue() # Levels of nodes for node ordering heuristics
        self.level = [0] * n # Positions of nodes in the node ordering
        self.rank = [0] * n

        for v in range(n):
            importance, shortcuts, level = self.shortcut(v)
            self.q.add(-importance, v)
        # Dijkstra search
        while not self.q.empty():
            v = q.pop()
            importance, shortcuts, level = self.shortcut(v)
        pass

    def mark_visited(self, x):
        if not self.visited[x]:
            self.visited[x] = True
            self.visited.append(x)

    def add_arc(self, u, v, c):
        def update(adj, cost, u, v, c):
            for i in range(len(adj[u])):
                if adj[u][i] == v:
                    cost[u][i] = min(cost[u][i], c)
                    return
            adj[u].append(v)
            cost[u].append(c)

        update(self.G[0], self.W[0], u, v, c)
        update(self.G[1], self.W[1], v, u, c)

    # Makes shortcuts for contracting node v
    def shortcut(self, v):
        # Implement this method yourself

        # Compute the node importance in the end
        shortcut_count = 0
        neighbors = 0
        shortcut_cover = 0
        level = 0
        # Compute correctly the values for the above heuristics before computing the node importance
        importance = (shortcut_count - len(self.adj[0][v]) - len(self.adj[1][v])) + neighbors + shortcut_cover + level
        return importance, shortcuts, level

    # See description of this method in the starter for friend_suggestion
    def clear():
        for v in self.visited:
            self.bidistance[0][v] = self.bidistance[1][v] = self.INFINITY
            self.visited[v] = False
        del self.visited[:]

    # See description of this method in the starter for friend_suggestion
    def visit(side, v, dist):
        # Implement this method yourself
        pass

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        q = [PriorityQueue(), PriorityQueue()]
        estimate = self.INFINITY
        visit(0, s, 0)
        visit(1, t, 0)
        # Implement the rest of the algorithm yourself

        return -1 if estimate == self.INFINITY else estimate


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

    ch = DistPreprocessSmall(n, adj, cost)
    print("Ready")
    sys.stdout.flush()
    t, = readl()
    for i in range(t):
        s, t = readl()
        print(ch.query(s-1, t-1))
