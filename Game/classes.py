from enum import Enum

class Dimension(Enum):
    WIDTH = 800
    HEIGHT = 600
    PIXEL = 20

class Color(Enum):
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
