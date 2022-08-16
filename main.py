from curses import COLOR_BLACK, COLOR_BLUE
from pickle import TRUE
import pygame

def direction(event, dir_x, dir_y):
    if event.type == pygame.KEYDOWN:
        match event.key:
            case pygame.K_LEFT:
                if dir_x != 10:
                    dir_x = -10
                    dir_y = 0
            case pygame.K_RIGHT:
                if dir_x != -10:
                    dir_x = 10
                    dir_y = 0
            case pygame.K_UP:
                if dir_y != 10:
                    dir_y = -10
                    dir_x = 0
            case pygame.K_DOWN:
                if dir_y != -10:
                    dir_y = 10
                    dir_x = 0
    return dir_x, dir_y

width = 800
height = 600

pygame.init()
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake in Python')
game_over = False

c_green = (0, 255, 0)

clock = pygame.time.Clock()

current_pos_X = width / 2
current_pos_Y = height / 2

direction_X = 0 # -10 for LEFT, +10 for RIGHT
direction_Y = 0 # -10 for DOWN, +10 for UP

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = TRUE
        direction_X, direction_Y = direction(event, direction_X, direction_Y)
    
    if current_pos_X == -10:
        current_pos_X = width - 10
    elif current_pos_X == width:
        current_pos_X = 0
    
    if current_pos_Y == -10:
        current_pos_Y = height - 10
    elif current_pos_Y == height:
        current_pos_Y = 0

    current_pos_X += direction_X
    current_pos_Y += direction_Y

    display.fill((0, 0, 0))
    pygame.draw.rect(display, c_green, [current_pos_X, current_pos_Y, 10, 10])
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()