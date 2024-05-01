import numpy as np
import heapq as pq
import mazeGeneration as mg
import time
start_time = time.time()
maxn = 100001
INF = 1e9
generator = mg.mazeGeneration()
matrix = generator.createMaze()
class maze_dijkstra_solving:
    def __init__(self) -> None:
        self.maze = generator.maze.copy()
        self.A_x = None
        self.A_y = None
        self.B_x = None
        self.B_y = None
        self.size = generator.size
        self.visited = None
        self.parent = None
        self.step = None
    def creatingInfo(self):
        self.parent = np.array([[None for i in range(self.size)] for j in range(self.size)])
        self.step = np.array([[INF for i in range(self.size)] for j in range(self.size)])
        self.A_x, self.A_y = 1, 1
        self.B_x, self.B_y = generator.size - 2 , generator.size - 2
        self.maze[self.A_x, self.A_y] = 'A'
        self.maze[self.B_x, self.B_y] = 'B'
    def Dijkstra(self):
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]   
        self.creatingInfo()     
        self.step[self.A_x, self.A_y] = 0
        Q = []
        pq.heappush(Q, (0, (self.A_x, self.A_y)))
        while(Q):
            top = pq.heappop(Q)
            kc = top[0]
            u = top[1]
            i = u[0]
            j = u[1]
            if(kc > self.step[u]): continue
            for k in range(4):
                newi = i + dx[k]
                newj = j + dy[k] 
                w = None
                if(newi >= 0 and newi < self.size) and (newj < self.size and newj >= 0) :
                    if(self.maze[newi, newj] == 'x'):
                        w = INF
                    else: w = 1
                if(self.step[newi, newj] > self.step[u] + w):
                    self.step[newi, newj] = self.step[u] + w
                    self.parent[newi, newj] = u
                    pq.heappush(Q, (self.step[newi, newj], (newi, newj)))
            if(self.maze[u] == 'B'):
                break
    def Truyvet(self):
        u, v = self.B_x, self.B_y
        if(self.step[self.B_x, self.B_y] != INF):
            print("Co duong di tu A den B")
            way = []
            way.append((u, v))
            while(u != self.A_x or v != self.A_y):
                temp = self.parent[u, v]
                u = temp[0]
                v = temp[1]
                way.append((u, v))
            way.reverse()
            return way
        

A = maze_dijkstra_solving()
A.Dijkstra()
path = A.Truyvet()
print("Process finished --- %s seconds ---" % (time.time() - start_time))
generator.matrix_pygame(path)
