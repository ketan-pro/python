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
car_w = img.get_width()

def blocks(color, T_X, T_Y, T_W, T_H):
    pygame.draw.rect(display, color, (T_X, T_Y, T_W, T_H))

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

    blk_start_x = random.randrange(0, SCREEN_W)
    blk_start_y = -600
    blk_speed = 7
    blk_w = 100
    blk_h = 100

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

        blocks(BLACK, blk_start_x, blk_start_y, blk_w, blk_h)
        blk_start_y += blk_speed
        
        car(car_x, car_y)

        if car_x > SCREEN_W - car_w or car_x < 0:
            crash() 

        if blk_start_y > SCREEN_H:
            blk_start_y = 0 - blk_h
            blk_start_x = random.randrange(0, SCREEN_W)

        if car_y < blk_start_y + blk_h:
            print('y crossover')

            if car_x > blk_start_x and car_x < blk_start_x + blk_w or car_x + car_w > blk_start_x and car_x + car_w < blk_start_x + blk_w:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
