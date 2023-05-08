import turtle
import random
import pygame
import math


def is_in_screen(w, t):
    return True

turt1 = turtle.Turtle()
turt1.speed(0)

wn = turtle.Screen

distance = 10
angle = 90

flipcoin = ["Heads","Tails"]
print (random.choice(flipcoin))
# is_in_screen = True

colors = ["red", "green", "blue", "purple", "red"]

#top down programming
while is_in_screen(wn, t):
    coin = random.randrange(0, 2)
    if coin: #heads
        turt1.right(angle)
    else: #tails
        turt1.left(angle)
    turt1.forward(distance)

    # turtleX = turt1.xcor()
    # turtleY = turt1.ycor()
    # # x, y = t.pos()

    # x_range = wn.window_width() / 2
    # y_range = wn.window_height() / 2

    # turt1.color(random.choice(colors))

    # if abs(turtleX) > x_range or abs(turtleY) > y_range:
    #     is_in_screen = False

wn.exitonclick()