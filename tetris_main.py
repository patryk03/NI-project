import turtle
import time
import random

class Shape:
    def __init__(self):
        self.y = 0
        self.x = 5
        self.color = random.randint(1, 7)
        square =[[1,1],
                [1,1]]

        hline = [[1,1,1,1]]

        vline =[[1],
                [1],
                [1],
                [1]]

        rightl =[[1,0,0,0],
                [1,1,1,1]]

        leftl =[[0,0,0,1],
                [1,1,1,1]]

        zshape =[[1,1,0],
                [0,1,1]]

        stairs =[[0,1,0],
                [1,1,1]]

        shapes = [square, hline, vline, rightl, leftl, zshape, stairs]

def draw_grid():
    pass


def draw_score():
    pass


def check_grid():
    pass
