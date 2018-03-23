#Uses python3

import sys
import heapq
from random import randint

class priorityQueue:

    def __init__(self):
        self.pq = list()
        self.finder = dict()

    def add(self, task, priority=0):
        if task in self.finder:
            self.remove(task)
        entry = [priority, task]
        self.finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove(self, task):
        entry = self.finder.pop(task)
        entry[0], entry[1] = float('inf'), None

    def pop(self):
        priority, task = heapq.heappop(self.pq)
        if task != None:
            del self.finder[task]
            return task

    def find(self, task):
        return self.finder.get(task, None)

    def empty(self):
        return len(self.finder) == 0

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
            if (PQ.find(z)!=None) and (cost[z]>w):
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