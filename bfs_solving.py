import numpy as np
import mazeGeneration as mg
import time
start_time = time.time()
matrix = mg.mazeGeneration().createMaze()

class Maze_bfs_solving:
    def __init__(self) -> None:
        self.maze = matrix.copy()
        self.A_x = None
        self.A_y = None
        self.B_x = None
        self.B_y = None
        self.size = mg.size
        self.visited = None
        self.parent = None
        self.step = None

    def createMaze(self):
        self.visited = np.array([[False for i in range(self.size)] for j in range(self.size)])
        self.parent = np.array([[None for i in range(self.size)] for j in range(self.size)])
        self.step = np.array([[0 for i in range(self.size)]for j in range(self.size)])
        self.A_x, self.A_y = 0 , 0
        self.B_x, self.B_y = self.size - 1 , self.size - 1

    def Bfs(self):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        self.createMaze()
        print(self.maze)
        s, t = self.A_x, self.A_y
        u, v = self.B_x, self.B_y
        queue = []
        queue.append((s, t))
        while(len(queue) > 0):
            top = queue.pop(0)
            #print(f"({top[0]}  {top[1]})")
            for k in range(4):
                i1 = top[0] + dx[k]
                j1 = top[1] + dy[k]
                if(i1 >= 0 and i1 < self.size and j1 >= 0 and j1 < self.size):
                    if(self.maze[top[0]][top[1]][k] != 1 and self.visited[i1, j1] == False):
                       #print(f"({i1}  {j1})")
                        self.step[i1, j1] = self.step[top[0], top[1]] + 1
                        self.parent[i1, j1] = (top[0], top[1])
                        if(i1 == self.B_x and j1 == self.B_y): return
                        queue.append((i1, j1))
                        self.visited[i1, j1] = True

    def Truyvet(self):
        if(self.step[self.B_x, self.B_y] != 0): 
            u, v = self.B_x, self.B_y
            way = []
            way.append((u, v))
            while(u != self.A_x or v != self.A_y):
                temp = self.parent[u, v]
                u = temp[0]
                v = temp[1]
                way.append((u,v))
            way.reverse()
            for step in way:
                print(step)
        print(self.step[self.B_x, self.B_y])
        return way
A = Maze_bfs_solving()
A.Bfs()
path = A.Truyvet()
print(path)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
mg.mazeApplication(matrix, path)
