#Uses python3

import sys
import heapq
from random import randint
import itertools

class priorityQueue:

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
        return self.entry_finder.get(task, self.REMOVED)

    def empty(self):
        return len(self.entry_finder) == 0

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)

def minimum_distance(x, y):
    n = len(x)
    cost, parent = list(), list()
    u = randint(0, n-1)
    PQ = priorityQueue()
    for i in range(n):
        c = float('inf')
        if i == u: c = 0
        cost.append(c)
        parent.append(None)
        PQ.add(i, cost[i])
    while not PQ.empty():
        v = PQ.pop()
        p1 = (x[v], y[v])
        for z in range(n):
            p2 = (x[z], y[z])
            w = distance(p1, p2)
            if (PQ.find(z)!=PQ.REMOVED) and (cost[z]>w):
                cost[z], parent[z] = w, v
                PQ.add(z, w)
    return float(sum(cost))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))