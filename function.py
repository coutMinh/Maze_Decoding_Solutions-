import pygame
screen = pygame.display.set_mode((1200, 696)) 
white = (255, 255, 255)
black=(0,0,0)
def draw_rectangle(x, y,width,text):
    font = pygame.font.Font(None, 36)
    white = (255, 255, 255)
    black = (0, 0, 0)
    rect = pygame.Rect(x, y, width,40)
    pygame.draw.rect(screen, black, rect)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + 20))
    screen.blit(text_surface, text_rect)