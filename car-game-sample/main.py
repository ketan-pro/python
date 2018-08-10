import time
import random
import pygame

pygame.init()

SCREEN_W = 800
SCREEN_H = 600
display = pygame.display.set_mode((SCREEN_W, SCREEN_H))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
pygame.display.set_caption("First game title")

clock = pygame.time.Clock()

img = pygame.image.load('car.png')
img_w = img.get_width()

def things(T_X, T_Y, T_W, T_H):
    pygame.draw.rect(display, BLACK, (T_X, T_Y, T_W, T_H))

def car(x, y):
    display.blit(img, (x,y))

def text_obj(txt, font):
    surface = font.render(txt, True, BLACK)
    return surface, surface.get_rect()

def msg_display(text):
    largeTxt = pygame.font.Font('freesansbold.ttf', 100)
    txtSurf, txtRect = text_obj(text, largeTxt)
    txtRect.center = ((SCREEN_W/2), (SCREEN_H/2))
    display.blit(txtSurf, txtRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash(): 
    msg_display('You Crashed')

def game_loop():
    car_x = SCREEN_W * 0.45
    car_y = SCREEN_H * 0.85
    car_x_change = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            print(event)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -5
                if event.key == pygame.K_RIGHT:
                    car_x_change = 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_x_change = 0
        
        car_x += car_x_change
        display.fill(WHITE)
        car(car_x, car_y)

        if car_x > SCREEN_W - img_w or car_x < 0:
            crash() 

        pygame.display.update()
        clock.tick(60)

game_loop()
