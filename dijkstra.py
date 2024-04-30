import numpy as np
import heapq as pq
maxn = 100001
INF = 1e9
class Dijkstra:
    def __init__(self) -> None:
        self.visited = [False for i in range(maxn)]
        self.step = [INF for i in range(maxn)]
        self.s = None
        self.n, self.m = None, None
        self.connection = [[] for i in range(maxn)]
    def inPut(self):
        self.n, self.m, self.s = map(int, input().split())
        for i in range(self.m):
            x, y, w = map(int, input().split())
            self.connection[x].append((y, w))
            self.connection[y].append((x, w))
    def dijstraSolving(self,s):
       Q = []
       self.step[self.s] = 0
       pq.heappush(Q, (0, self.s))
       while Q:
            temp = pq.heappop(Q)
            kc = temp[0]
            u = temp[1]
            if temp[0] > self.step[temp[1]]: continue
            for neighbor in self.connection[u]:
                v = neighbor[0]
                w = neighbor[1]
                if(self.step[v] > self.step[u] + w):
                    self.step[v] = self.step[u] + w
                    pq.heappush(Q, (self.step[v], v))
        


