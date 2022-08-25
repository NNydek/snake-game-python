import pygame
from Game.classes import Dimension

width = Dimension.WIDTH.value
height = Dimension.HEIGHT.value

title = pygame.display.set_caption('Snake in Python')
screen = pygame.display.set_mode((width, height))
timer = pygame.time.Clock()
