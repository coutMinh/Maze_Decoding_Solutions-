import pygame
import random
from pygame.locals import *
import function as fc
import gameplay
def menu():
    pygame.init() 
    # displaying Canvas (960*600) 
    infoObject = pygame.display.Info()
    window_size = (infoObject.current_w - 30, infoObject.current_h - 50)
    screen = pygame.display.set_mode((1300, 900)) 
    x_move, y_move = 200,200
    white = (255, 255, 255)
    black=(0,0,0)
    loop1=True
    while loop1:
        image = pygame.image.load("image/41524.jpg")  # Thay đổi đường dẫn đến ảnh của bạn
        image_rect = image.get_rect()
        for event in pygame.event.get():
            screen.blit(image, image_rect) 
            if event.type == pygame.QUIT: 
                loop1 = False
            fc.draw_rectangle(540,348,100,"Play")
            fc.draw_rectangle(540,348+50,100,"Exit")
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    x1,y1=event.pos
                    print("Chuot trai duoc nhan tai vi tri: ",event.pos)
                    if (541<=x1&x1<=639)&(350<=y1&y1<=385):
                        loop1=False
                        #gameplay.mazeSolving()
                    if (541<=x1&x1<=639)&(400<=y1&y1<=436):
                        loop1=False
        pygame.display.flip()
if __name__ == "__main__":
    menu()
    A = gameplay.game()
    A.mazeSolving()
