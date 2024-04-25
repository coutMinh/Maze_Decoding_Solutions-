import numpy as np
class Maze_bfs_solving:
    def __init__(self) -> None:
        self.maze = None
        self.A_x = None
        self.A_y = None
        self.B_x = None
        self.B_y = None
    def createRandomMaze(self):
        self.maze = np.random.randint(0,2, size = (12,12))
        cond1 = self.maze > 0
        self.maze = np.where(cond1, 'x', 'o')
        random_indexing = list(map(int, np.random.randint(0,12, size = (1,4))[0]))
        self.A_x, self.A_y, self.B_x, self.B_y = map(int, random_indexing)
        self.maze[self.A_x, self.A_y] = 'A'
        self.maze[self.B_x, self.B_y] = 'B'
    def Bfs(self):
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        self.createRandomMaze()
        print(self.maze)
        s, t = self.A_x, self.A_y
        u, v = self.B_x, self.B_y
        queue = []
        queue.append((s, t))
        while(len(queue) > 0):
            top = queue.pop(0)
            i, j = top[0], top[1]
            #for i in range(4):





A = Maze_bfs_solving()
A.Bfs()


