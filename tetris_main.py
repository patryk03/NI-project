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


def check_grid(grid):
    #check if bottom row is full
    y = 23
    while y > 0: 
        is_full = True
        for x in range(0,12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break

        if is_full:
            global score
            score += 10
            draw_score(pen, score)
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y - 1][copy_x]
<<<<<<< konflikty
def move_left(grid):
    # Chech if it is possible to move left
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                if x == 0 or grid[y][x - 1] != 0:
                    return  
<<<<<<< main
    # Move left
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                grid[y][x - 1] = grid[y][x]  
                grid[y][x] = 0  

           

def draw_score():
    pass


def check_grid():
    pass
        
def move_left(grid):
        pass



#dopisac w komentarzu co jeszcze opracować
