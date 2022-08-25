import pygame
from Food import food
from Game.classes import Color, Dimension
from Snake.movement import get_direction, pass_through_border
from . import game_window

def start():
    pygame.init()

    width = Dimension.WIDTH.value
    height = Dimension.HEIGHT.value
    pixel = Dimension.PIXEL.value

    display = game_window.screen
    clock = game_window.timer

    game_over = False
    game_speed = 30     # Frames per second

    current_pos_x = width / 2    # Starting Position
    current_pos_y = height / 2   # in a middle of a window

    direction_x = 0     # -PIXEL for LEFT, +PIXEL for RIGHT
    direction_y = 0     # -PIXEL for DOWN, +PIXEL for UP

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            direction_x, direction_y = get_direction(event, direction_x, direction_y, pixel)

        current_pos_x += direction_x
        current_pos_y += direction_y

        current_pos_x, current_pos_y = pass_through_border(current_pos_x, current_pos_y, pixel)

        display.fill(Color.BLACK.value)
        pygame.draw.rect(display, Color.RED.value, [food.x, food.y, pixel, pixel])
        pygame.draw.rect(display, Color.GREEN.value, [current_pos_x, current_pos_y, pixel, pixel])
        
        if current_pos_x == food.x and current_pos_y == food.y:
            food.x, food.y = food.generate()

        pygame.display.update()
        clock.tick(game_speed)
    pygame.quit()
