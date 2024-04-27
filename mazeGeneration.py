import numpy as np
import pygame
import random
class mazeGeneration:

    def __init__(self) -> None:
        self.maze = None
        self.A_x = None
        self.A_y = None
        self.B_x = None
        self.B_y = None
        self.parent = None
        self.dx = [-2, 0, 0 ,2]
        self.dy = [0, -2, 2, 0]
        self.size = 25
        self.visited = None

    def createMaze(self):
        self.parent = np.array([[None for i in range(self.size)]for j in range(self.size)])
        self.maze = np.array([['x' for i in range(self.size)] for j in range(self.size)])
        self.maze[1:self.size - 1:2, 1:self.size - 1:2] = 'o'
        self.visited = np.array([[False for i in range(self.size)]for j in range(self.size)])
        #print(self.maze)
        print(self.visited)
        self.dfs(1,1)
        print(self.visited)
        self.maze[self.visited] = 'o'
        return self.maze

    def dfs(self, s, t):
        self.visited[s, t] = True
        parent = self.parent[s, t]
        if(parent != None):
            self.visited[(s + parent[0])//2, (t + parent[1]) // 2] = True
        self.maze[s, t] = 'x'
        way = [0,1,2,3]
        while(len(way) > 0):
            k = random.choice(way)
            way.remove(k)
            s1 = s + self.dx[k]
            t1 = t + self.dy[k]
            if(s1 >= 0 and s1 < self.size and t1 >= 0 and t1 < self.size and self.visited[s1,t1] == False and self.maze[s1, t1] == 'o'):
                self.parent[s1, t1] = (s, t)
                self.dfs(s1, t1)


def matrix_pygame(maze_matrix: np.array):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    # Kích thước của mê cung và các ô
    rows = maze_matrix.shape[0]
    cols = maze_matrix.shape[1]
    # Chia tỷ lệ kích thước ô để hiển thị trên màn hình
    scale_factor = 2
    cell_size = 30 // scale_factor  # Thu nhỏ kích thước của ô
    # Khởi tạo Pygame
    pygame.init()

    # Kích thước cửa sổ
    window_size = ((cols) * cell_size, (rows) * cell_size)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Maze")

    # Màu nền
    screen.fill(WHITE)

    # Vẽ mê cung từ ma trận
    for i in range(rows):
        for j in range(cols):
            color = BLACK if maze_matrix[i][j] == 'x' else WHITE
            pygame.draw.rect(screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))

    # Hiển thị mê cung
    pygame.display.flip()

    # Vòng lặp chính
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Kết thúc Pygame
    pygame.quit()

A = mazeGeneration()
matrix = A.createMaze()
matrix_pygame(matrix)