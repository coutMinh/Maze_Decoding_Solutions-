import random
import pygame
import numpy as np

size = 15 # size 15x15
cell_size = 15  # Kích thước của mỗi ô trong mê cung
screen_width, screen_height = 1200, 900 #1200, 900
screen = pygame.display.set_mode((screen_width, screen_height))
white, black = (255, 255, 255), (0, 0, 0)

class mazeGeneration:

    def __init__(self) -> None:
        self.maze = None
        self.A_x = None
        self.A_y = None
        self.B_x = None
        self.B_y = None
        self.parent = None
        self.dx = [1, 0, -1 ,0]
        self.dy = [0, 1, 0, -1]
        self.size = size
        self.visited = None

    def createMaze(self):
        self.parent = np.array([[None for i in range(self.size)]for j in range(self.size)])
        self.maze = [[[1 for i in range(4)] for i in range(self.size)] for j in range(self.size)]
        self.visited = np.array([[False for i in range(self.size)]for j in range(self.size)])
        #print(self.maze)
        self.dfs(0, 0)
        #print(self.visited)
        return self.maze

    def dfs(self, s, t):
        self.visited[s, t] = True
        way = [0,1,2,3]
        while(len(way) > 0):
            k = random.choice(way)
            way.remove(k)
            s1 = s + self.dx[k]
            t1 = t + self.dy[k]
            if(s1 >= 0 and s1 < self.size and t1 >= 0 and t1 < self.size and self.visited[s1,t1] == False):
                self.maze[s][t][k] = 0
                if k == 0: self.maze[s1][t1][2] = 0    
                if k == 1: self.maze[s1][t1][3] = 0   
                if k == 2: self.maze[s1][t1][0] = 0   
                if k == 3: self.maze[s1][t1][1] = 0                 
                self.dfs(s1, t1)

def draw_maze(Walls):
    # Tính toán tọa độ bắt đầu vẽ mê cung để canh chỉnh vào giữa màn hình
    maze_width = size * cell_size
    maze_height = size * cell_size
    start_x = (screen_width - maze_width) // 2
    start_y = (screen_height - maze_height) // 2

    for x in range(size):
        for y in range(size):
            if Walls[y][x][3] == 1:  # Tường bên trái
                pygame.draw.line(screen, black, (start_x + x * cell_size, start_y + y * cell_size),
                                 (start_x + x * cell_size, start_y + (y + 1) * cell_size))
            if Walls[y][x][2] == 1:  # Tường phía trên
                pygame.draw.line(screen, black, (start_x + x * cell_size, start_y + y * cell_size),
                                 (start_x + (x + 1) * cell_size, start_y + y * cell_size))
            if Walls[y][x][1] == 1:  # Tường bên phải
                pygame.draw.line(screen, black, (start_x + (x + 1) * cell_size, start_y + y * cell_size),
                                 (start_x + (x + 1) * cell_size, start_y + (y + 1) * cell_size))
            if Walls[y][x][0] == 1:  # Tường phía dưới
                pygame.draw.line(screen, black, (start_x + x * cell_size, start_y + (y + 1) * cell_size),
                                 (start_x + (x + 1) * cell_size, start_y + (y + 1) * cell_size))


def mazeApplication(Walls, path):
    maze_width = size * cell_size
    maze_height = size * cell_size
    start_x = (screen_width - maze_width) // 2
    start_y = (screen_height - maze_height) // 2
    # Khởi tạo màn hình Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Tạo màn hình
    screen.fill(white)

    # Vẽ mê cung
    draw_maze(Walls)

    # Hiển thị mê cung
    pygame.display.flip()

    # Vòng lặp chính
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for i in range(len(path) - 1):
                start = (start_x + path[i][1] * cell_size + cell_size // 2,start_y + path[i][0] * cell_size + cell_size // 2)
                end = (start_x + path[i + 1][1] * cell_size + cell_size // 2,start_y + path[i + 1][0] * cell_size + cell_size // 2)
                pygame.draw.line(screen, (255, 0, 0), start, end, 3)
        pygame.display.flip()
        # Đặt tốc độ hiển thị
        clock.tick(60)

    pygame.quit()

