import turtle
import time
import random

wn = turtle.Screen()
wn.title("tetris")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0) #turns off the screen updates

delay = 0.1
slow_down = False


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
        def move_left(self, grid): 
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1


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


           

def draw_score():
    pass


def check_grid():
    pass
        

def power_up():
    global slow_down
    slow_down = True
    pen.speed(0)
    # Ustaw czas trwania spowolnienia (np. 5 sekund)
    time.sleep(5)
    pen.speed(5)
    slow_down = False



#dopisac w komentarzu co jeszcze opracować
