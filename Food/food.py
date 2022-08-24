import random
from Game.classes import Dimension

width = Dimension.WIDTH.value
height = Dimension.HEIGHT.value
pixel = Dimension.PIXEL.value

def generate():
    new_x = round(random.randrange(0, width - pixel) / pixel) * pixel
    new_y = round(random.randrange(0, height - pixel) / pixel) * pixel
    return new_x, new_y
x, y = generate()

