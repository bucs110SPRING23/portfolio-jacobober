import turtle
import random
import pygame
import math

#Part A
turt1 = turtle.Turtle()
turt2 = turtle.Turtle()

turt1.penup()
turt1.speed(1)
turt2.penup()
turt2.speed(1)

turt1.setposition(-100,20)
turt2.setposition(-100,-20)
    #Race 1
window = turtle.Screen()

turt1.forward(random.randrange(1, 101))
turt2.forward(random.randrange(1, 101))

turt1.goto(-100,20)
turt2.goto(-100,-20)

    #Race 2
for x in range(10):
    turt1.forward(random.randrange(1, 10))
    turt2.forward(random.randrange(1, 10))

turt1.goto(-100,20)
turt2.goto(-100,-20)

window.exitonclick()

#Part B
pygame.init()
window = pygame.display.set_mode()

xpos = 100
ypos = 100
side_length = 100
shapes = [3, 4, 6, 20, 100, 360]

for num_sides in shapes:
    
    points = []

    for i in range(num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])
    pygame.draw.polygon(window, 'red', points)
    pygame.display.flip()
    window.fill('Blue')
    pygame.time.wait(2000)

# for i in [1,2,3,4]:
#     print(i)]