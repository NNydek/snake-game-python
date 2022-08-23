import sys
import getopt
import pygame
import game_window
import food
from classes import Color, Dimension
from functions import get_direction, pass_through_border

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "h", ["help"])
        except getopt.error as msg:
             raise Usage(msg)
    except Usage as err:
        print >>sys.stderr, err.msg
        print >>sys.stderr, "for help use --help"
        return 2
    
    pygame.init()

    width = Dimension.WIDTH.value
    height = Dimension.HEIGHT.value
    pixel = Dimension.PIXEL.value

    display = game_window.screen
    clock = game_window.timer

    game_over = False
    game_speed = 30     # Frames per second

    current_pos_X = width / 2    # Starting Position
    current_pos_Y = height / 2   # in a middle of a window

    direction_X = 0     # -PIXEL for LEFT, +PIXEL for RIGHT
    direction_Y = 0     # -PIXEL for DOWN, +PIXEL for UP

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            direction_X, direction_Y = get_direction(event, direction_X, direction_Y, pixel)
                
        current_pos_X, current_pos_Y = pass_through_border(current_pos_X, current_pos_Y, pixel)

        current_pos_X += direction_X
        current_pos_Y += direction_Y

        display.fill(Color.BLACK.value)
        pygame.draw.rect(display, Color.RED.value, [food.x, food.y, pixel, pixel])
        pygame.draw.rect(display, Color.GREEN.value, [current_pos_X, current_pos_Y, pixel, pixel])
        
        if current_pos_X == food.x and current_pos_Y == food.y:
            food.x, food.y = food.generate()

        pygame.display.update()
        clock.tick(game_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    sys.exit(main())