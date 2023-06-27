import turtle
import time
import random
<<<<<<<< second_branch_for_conflict
class Shape:
        def __init__(self):
                self.y = 0
                self.x = 5
                self.color = random.randint(1, 7)
                square =[[1,1],
<<<<<<< the conflict should be                        
                [1,1]]

                rightl =[[1,0,0,0],




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

>>>> main
def check_grid(grid):
    #check if bottom row is full
    y = 23
    while y > 0: 
test
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



#dopisac w komentarzu co jeszcze opracować
