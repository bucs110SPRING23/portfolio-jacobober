import turtle
# from turtle import Turtle


sides = int(input("Enter the number of sides: "))
length= int(input("Enter the length of each side: "))
pen = turtle.Turtle()
pen.color("blue")

window = turtle.Screen()

for s in range(sides):
    pen.forward(length)
    pen.right(360/sides)


window.exitonclick()