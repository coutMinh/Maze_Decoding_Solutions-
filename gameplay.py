import pygame
import random
from pygame.locals import *
import mazeGeneration as mg
class game:
    def __init__(self) -> None:
        self.screen = None
        self.size = None
        self.matrix = None
    def creatingMaze(self):
        generator = mg.mazeGeneration()
        self.matrix = generator.createMaze()
        self.size = len(self.matrix)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        # Kích thước của mê cung và các ô
        rows = self.matrix.shape[0]
        cols = self.matrix.shape[1]
        # Chia tỷ lệ kích thước ô để hiển thị trên màn hình
        scale_factor = 2
        cell_size = 30 // scale_factor  # Thu nhỏ kích thước của ô
        # Khởi tạo Pygame
        pygame.init()

        # Kích thước cửa sổ
        window_size = ((cols) * cell_size, (rows) * cell_size)
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("Maze")
        cell_width = self.screen.get_width() // cols
        cell_height = self.screen.get_height() // rows
        # Màu nền
        self.screen.fill(WHITE)

        # Vẽ mê cung từ ma trận
        for i in range(rows):
            for j in range(cols):
                color = BLACK if self.matrix[i][j] == 'x' else WHITE
                pygame.draw.rect(self.screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
        # Hiển thị mê cung
        pygame.display.flip()
    def mazeSolving(self):
        self.creatingMaze()
        player_x, player_y = 1, 1 
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        loop2 = True
        rows = self.matrix.shape[0]
        cols = self.matrix.shape[1]
        scale_factor = 2
        cell_size = 30 // scale_factor  # Thu nhỏ kích thước của ô
        while loop2:
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    loop2 = False
                elif event.type == pygame.KEYDOWN:
                    passx, passy = player_x, player_y
                    if event.key == pygame.K_LEFT and player_y > 0 and self.matrix[player_x, player_y - 1] == 'o':
                        player_y -= 1
                    elif event.key == pygame.K_RIGHT and player_y < cols - 1 and self.matrix[player_x, player_y + 1] == 'o':
                        player_y += 1
                    elif event.key == pygame.K_UP and player_x > 0 and self.matrix[player_x - 1, player_y] == 'o':
                        player_x -= 1
                    elif event.key == pygame.K_DOWN and player_x < rows - 1 and self.matrix[player_x + 1, player_y] == 'o':
                        player_x += 1
                    if passx != player_x or passy != player_y:
                        self.matrix[player_x, player_y] = 's'
                        self.matrix[passx, passy] = 'o'
                    for i in range(rows):
                        for j in range(cols):
                            if self.matrix[i][j] == 'x':
                                color = BLACK
                            elif self.matrix[i, j] == 's':
                                color = RED
                            else:
                                color = WHITE
                            pygame.draw.rect(self.screen, color, (j * cell_size, i * cell_size, cell_size, cell_size))
                    pygame.display.flip()
        pygame.quit()
A = game()
A.mazeSolving()
