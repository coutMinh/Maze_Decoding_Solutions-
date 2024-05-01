import numpy as np
import mazeGeneration as mg
import time
start_time = time.time()
generator = mg.mazeGeneration()
matrix = generator.createMaze()

class Maze_bfs_solving:
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

    def createMaze(self):
        self.visited = np.array([[False for i in range(self.size)] for j in range(self.size)])
        self.parent = np.array([[None for i in range(self.size)] for j in range(self.size)])
        self.step = np.array([[0 for i in range(self.size)]for j in range(self.size)])
        self.A_x, self.A_y = 1, 1
        self.B_x, self.B_y = generator.size - 2 , generator.size - 2
        self.maze[self.A_x, self.A_y] = 'A'
        self.maze[self.B_x, self.B_y] = 'B'

    def Bfs(self):
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
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
                    if(self.maze[i1, j1] != 'x'):
                       #print(f"({i1}  {j1})")
                        self.step[i1, j1] = self.step[top[0], top[1]] + 1
                        self.parent[i1, j1] = (top[0], top[1])
                        if(self.maze[i1, j1] == 'B'): return
                        queue.append((i1, j1))
                        self.maze[i1, j1] = 'x'

    def Truyvet(self):
        if(self.step[self.B_x, self.B_y] != 0): 
            print("Co duong di tu A den B")
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
        else: print("Khong co duong di tu A den B") 
        print(self.step[self.B_x, self.B_y])
        return way
A = Maze_bfs_solving()
A.Bfs()
path = A.Truyvet()
print("Process finished --- %s seconds ---" % (time.time() - start_time))
generator.matrix_pygame(path)

