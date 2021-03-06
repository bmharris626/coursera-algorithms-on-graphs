#Uses python3

import sys

def explore(v, visited, ccNum, E):
    visited[v] = True
    ccNum[v] = 1
    for w in E[v]:
        if not visited[w]: explore(w, visited, ccNum, E)

def number_of_components(adj):
    cc = 0
    visited = [False for i in range(len(adj))]
    ccNum = [0 for i in range(len(adj))]
    for v in range(len(adj)):
        if not visited[v]:
            explore(v, visited, ccNum, adj)
            cc += 1
    return cc

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
    print(number_of_components(adj))
