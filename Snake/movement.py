from Game.classes import Dimension
import pygame

width = Dimension.WIDTH.value
height = Dimension.HEIGHT.value
pixel = Dimension.PIXEL.value

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
    if x < 0:
        x = width - pixel
    elif x == width:
        x = 0
    
    if y < 0:
        y = height - pixel
    elif y == height:
        y = 0
    return x, y

