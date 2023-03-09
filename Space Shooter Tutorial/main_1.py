import pygame
import os 
import time 
import random

WIDTH, HEIGHT = 750, 750

player_x = 0
player_y = 0

class Ship:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y 
        self.img = img

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Codinglab")

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))
player_img = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
enemy_img = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))

player = Ship(100, 100, player_img)
#enemy = Ship(200, 200, enemy_img)
enemyCnt = 0
enemies = []
#enemy = Ship(random.randrange(50, WIDTH-100), 0, RED_SPACE_SHIP)
run = True
while run:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:# and player_x - 5 > 0: # left
        #player_x -= 5
        player.move(-5, 0)
    if keys[pygame.K_RIGHT]: # and player_x + 5 < WIDTH: # right
        #player_x += 5
        player.move(5, 0)
    if keys[pygame.K_UP]: #and player_y - 5 > 0: # up
        #player_y -= 5
        player.move(0, -5)
    if keys[pygame.K_DOWN]:# and player_y + 5  < HEIGHT: # down
        #player_y += 5
        player.move(0, 5)

    window.blit(BG, (0,0))
    #window.blit(YELLOW_SPACE_SHIP, (player_x,player_y))
    player.draw(window)
    enemy.draw(window)
    pygame.display.update()
pygame.quit()