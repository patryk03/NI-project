import turtle
import time
import random

wn = turtle.Screen()
wn.title("tetris")
wn.bgcolor("black")
wn.setup(width=600, height=800)
wn.tracer(0) #turns off the screen updates

delay = 0.1



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

        def move_left(self, grid):
            if self.x > 0:
                if grid[self.y][self.x - 1] == 0:
                    self.erase_shape(grid)
                    self.x -= 1

        def move_right(self, grid):
            if self.x < 12 - self.width:
                if grid[self.y][self.x + self.width] == 0:
                    self.erase_shape(grid)
                    self.x += 1

        def draw_shape(self, grid):
            for y in range(self.height):
                for x in range(self.width):
                    if (self.shape[y][x] == 1):
                        grid[self.y + y][self.x + x] = self.color

        def erase_shape(self, grid):
            for y in range(self.height):
                for x in range(self.width):
                    if (self.shape[y][x] == 1):
                        grid[self.y + y][self.x + x] = 0

        def can_move(self, grid):
            result = True
            for x in range(self.width):
                # check if bottom is a 1
                if (self.shape[self.height - 1][x] == 1):
                    if (grid[self.y + self.height][self.x + x] != 0):
                        result = False
            return result

        def rotate(self, grid):
            self.erase_shape(grid)
            rotated_shape = []
            for x in range(len(self.shape[0])):
                new_row = []
                for y in range(len(self.shape) - 1, -1, -1):
                    new_row.append(self.shape[y][x])
                rotated_shape.append(new_row)

            right_side = self.x + len(rotated_shape[0])
            if right_side < len(grid[0]):
                self.shape = rotated_shape
                # update height and width
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


def draw_score(pen, score):
    pen.hideturtle()
    pen.goto(100,200)
    pen.write("score: {}".format(score), move=False, align="left", font=("Arial", 18, "normal"))

#creating the shape
shape = Shape()

#putting the shape to the grid
for y in range(shape.height):
    for x in range(shape.width):
        grid[shape.y+y][shape.x+x] = shape.color

#drawing initial grid
#draw_grid(pen, grid)



wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), chr(97)) #chr(97) = add
wn.onkeypress(lambda: shape.move_right(grid), "d")
wn.onkeypress(lambda: shape.rotate(grid), "space")


#score to 0
score = 0

draw_score(pen, score)


#main game loop
while True:
    wn.update()

    #moving the shape
    #next_cell = shape.y + 1
    if shape.y == 23 - shape.height + 1:
        shape = Shape() #kiedy ksztalt jest na samym dole, tworzy sie nowy 
        check_grid(grid) #chek if the row is filled

    elif shape.can_move(grid): #kiedy napotka niezerowa komorke zatrzyma sie lub kiedy napotka 23. wiersz grida
        shape.erase_shape(grid)
        
        shape.y += 1

        shape.draw_shape(grid)


    else:
        shape = Shape()
        check_grid(grid)
        

    draw_score(pen, score)
    draw_grid(pen, grid)
    #check_full(grid, row, licznik)
    

    time.sleep(delay)



wn.mainloop()




