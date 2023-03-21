import turtle

# Define the draw_house function
def draw_house(turt, size, color):
    """
    This function draws a house with the specified color and size from the user.
    
    args:     
    turt (turtle.Turtle): The turtle object used to draw the house.
    size (int): The size of the house.
    color (str): The color of the house.

    returns: size (int): The size of the house
    """
    turt.color(color)
    turt.begin_fill()

    # Draw the main house
    turt.forward(size * 4)
    turt.right(90)
    turt.forward(size * 3)
    turt.right(90)
    turt.forward(size * 4)
    turt.right(90)
    turt.forward(size * 3)
    turt.right(90)

    # Draw the roof
    turt.color("red")
    turt.penup()
    turt.goto(size * 4, 0)
    turt.pendown()
    turt.begin_fill()
    turt.goto((size * 4) / 2, size * 3)
    turt.goto(0, 0)
    turt.end_fill()

    # Draw the door
    turt.color("brown")
    turt.penup()
    turt.goto(size * 1.5, -size)
    turt.pendown()
    turt.begin_fill()
    turt.forward(size * 1.15)
    turt.right(90)
    turt.forward(size * 2)
    turt.right(90)
    turt.forward(size * 1.15)
    turt.right(90)
    turt.forward(size * 2)
    turt.right(90)
    turt.end_fill()

    # Draw the doorknob
    turt.color("yellow")
    turt.penup()
    turt.goto(size * 2.25, -1.75 * size)
    turt.pendown()
    turt.dot(size / 5)
    turt.end_fill()
    
    # Return the size of the house
    return size

# Define the circle function
def circle(turt, size):
    """
    Draws a circle with the size returned from drawing the house. (Uses as radius)
    
    args:
    turt (turtle.Turtle): The turtle object used to draw the circle.
    size (int): The size of the circle.
    
    returns: None
    """
    # Move the turtle to the top-left corner
    turt.penup()
    turt.goto(-size * 2, size * 3)
    turt.pendown()

    # Draw Circle
    turt.circle(size)

# Define the main function
def main():
    # Create a turtle object
    turt = turtle.Turtle()

    # Ask the user for input
    size = int(input("Enter the size of the house: "))
    color = input("Enter the color of the house: ")

    # Draw the house and get the size of the house
    house_size = draw_house(turt, size, color)

    #Draw the circle using the size of the house
    circle(turt, house_size)

    # Hide the turtle
    turt.hideturtle()

    # Print the size of the house
    print("The house is", house_size, "units long.")

    # Keep the window open until manually closed
    turtle.exitonclick()
    
# Call the main function
main()