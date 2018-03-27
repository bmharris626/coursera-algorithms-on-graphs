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

    def find(self, task):
        return self.entry_finder.get(task, None)

    def empty(self):
        return len(self.entry_finder) == 0

class AStar:
    def __init__(self, n, adj, cost, x, y):
        # See the explanations of these fields in the starter for friend_suggestion
        self.n = n
        self.G = adj
        self.W = cost
        self.inf = n*10**6
        self.gScore = [self.inf]*n
        self.workset = []
        self.x = x
        self.y = y

    def distance(self, u, v):
        return ((x[u]-x[v])**2 + (y[u]-y[v])**2)**(1/2)

    # See the explanation of this method in the starter for friend_suggestion
    def clear(self):
        for v in self.workset:
            self.gScore[v] = self.inf
        del self.workset[0:len(self.workset)]

    # Returns the distance from s to t in the graph
    def query(self, start, goal):
        self.clear()
        openSet = PriorityQueue()
        openSet.add(start, 0)
        self.gScore[start] = 0
        self.workset.append(start)
        closedSet = list()
        while not openSet.empty():
            current = openSet.pop()
            if current == goal: return self.gScore[current]
            for i in range(len(self.G[current])):
                neighbor = self.G[current][i]
                if neighbor in closedSet: continue
                tentative_gScore = self.gScore[current] + self.W[current][i]
                if tentative_gScore >= self.gScore[neighbor]: continue
                self.gScore[neighbor] = tentative_gScore
                priority = self.gScore[neighbor] + self.distance(neighbor, goal)
                openSet.add(neighbor, priority)
                self.workset.append(neighbor)
        return -1

def readl():
    return map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    n,m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u,v,c = readl()
        adj[u-1].append(v-1)
        cost[u-1].append(c)
    t, = readl()
    astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        print(astar.query(s-1, t-1))
