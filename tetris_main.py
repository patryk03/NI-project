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

                self.shape = random.choice(shapes)

                self.height = len(self.shape) 
                self.width = len(self.shape[0])
        
        # def move_left(self, grid): 
        # def move_right(self, grid):
        # def draw_shape(self, grid):
        # def erase_shape(self, grid):
        # def can_move(self, grid):
        # def rotate(self, grid):


grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]



pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None) #nadlatuja nowe bloki




def draw_grid(pen, grid):
    pen.clear() #czysci wszytsko z ekranu
    top = 230
    left = -190 #ustawienie ekranu

    colors = ["darkgrey", "lightblue", "blue", "orange", "yellow", "green", "red", "purple"]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x*20)
            screen_y = top - (y*20)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()


            

def draw_score():
    pass


def check_grid():
    pass
