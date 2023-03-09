import pygame
#import os 
#import time 
import random

WIDTH, HEIGHT = 750, 750

window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Codinglab")

image = pygame.image.load("assets/pixel_ship_yellow.png").convert_alpha()
BG = pygame.transform.scale((pygame.image.load("assets/background-black.png")), (WIDTH, HEIGHT))
enemy = pygame.image.load("assets/pixel_ship_blue_small.png")



x = 200
y = 200

enemy_x = 0
enemy_y = 0

run = True
while run:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            run = False
            
    pressed = pygame.key.get_pressed()
   
    if pressed[pygame.K_LEFT]:
        x -= 5
    elif pressed[pygame.K_RIGHT]:
        x += 5
    eenmy_x = random.randrange(1, 750)    
    window.blit(BG, (0,0))
    window.blit(image, (x, y))  
    window.blit(enemy, (enemy_x, enemy_y))  
    #nn_layer.training()   

    pygame.display.update()
pygame.quit()