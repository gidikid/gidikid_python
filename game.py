import pygame
import random


pygame.init


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("simple game")


player_width = 50
player_height =50
player_x = screen_width/2 - player_width/2
player_y = screen_height/2 - player_height/2
player_speed = 5

player = pygame.Rect(player_x,player_y,player_width,player_height)


enemy_width = 50
enemy_height = 50
enemy_x =random.randint(0, screen_width -enemy_width)
enemy_y =0
enemy_speed = 2
enemy = pygame.Rect(enemy_x,enemy_y,enemy_width,enemy_height)

font = pygame.font.Font(None, 36)



score = 0

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running - False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0 :
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x > screen_width -player_width :
        player_x += player_speed    