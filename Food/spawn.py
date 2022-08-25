import pygame
import random
from Game.classes import Color, Dimension
from Game import game_window

width = Dimension.WIDTH.value
height = Dimension.HEIGHT.value
pixel = Dimension.PIXEL.value

def generate_food():
    new_x = round(random.randrange(0, width - pixel) / pixel) * pixel
    new_y = round(random.randrange(0, height - pixel) / pixel) * pixel
    return new_x, new_y

x, y = generate_food()

def draw_food(x, y):
    pygame.draw.rect(game_window.screen, Color.RED.value, [x, y, pixel, pixel])
