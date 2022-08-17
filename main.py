from enum import Enum
import pygame

class Color(Enum):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

def get_direction(event, dir_x, dir_y, pixel):
    if event.type == pygame.KEYDOWN:
        match event.key:
            case pygame.K_LEFT:
                if dir_x != pixel:
                    dir_x = -pixel
                    dir_y = 0
            case pygame.K_RIGHT:
                if dir_x != -pixel:
                    dir_x = pixel
                    dir_y = 0
            case pygame.K_UP:
                if dir_y != pixel:
                    dir_y = -pixel
                    dir_x = 0
            case pygame.K_DOWN:
                if dir_y != -pixel:
                    dir_y = pixel
                    dir_x = 0
    return dir_x, dir_y

def pass_through_border(x, y, pixel):
    if x == -pixel:
        x = width - pixel
    elif x == width:
        x = 0
    
    if y == -pixel:
        y = height - pixel
    elif y == height:
        y = 0
    return x, y

width = 800
height = 600
pixel = 10

pygame.init()
pygame.display.set_caption('Snake in Python')
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

game_over = False
game_speed = 30

current_pos_X = width / 2    # Starting Position
current_pos_Y = height / 2   # in a middle of a window

direction_X = 0     # -pixel for LEFT, +pixel for RIGHT
direction_Y = 0     # -pixel for DOWN, +pixel for UP

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        direction_X, direction_Y = get_direction(event, direction_X, direction_Y, pixel)
    
    current_pos_X, current_pos_Y = pass_through_border(current_pos_X, current_pos_Y, pixel)

    current_pos_X += direction_X
    current_pos_Y += direction_Y

    display.fill(Color.BLACK.value)
    pygame.draw.rect(display, Color.GREEN.value, [current_pos_X, current_pos_Y, pixel, pixel])
    
    pygame.display.update()
    clock.tick(game_speed)

pygame.quit()
quit()