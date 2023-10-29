import turtle

# Function to generate the Dragon Curve
def dragon_curve(order, length, direction=1):
    if order == 0:
        turtle.forward(length)
    else:
        length /= (2 ** 0.5)
        turtle.left(45 * direction)
        dragon_curve(order - 1, length, 1)
        turtle.right(90 * direction)
        dragon_curve(order - 1, length, -1)
        turtle.left(45 * direction)

# Initialize the Turtle
turtle.speed(0)  # Fastest drawing speed
turtle.penup()
turtle.goto(-150, 0)
turtle.pendown()

# Set the order and length for the Dragon Curve
order = 10  # You can adjust this to change the level of detail
length = 300

# Draw the Dragon Curve
dragon_curve(order, length)

# Close the Turtle graphics window on click
turtle.exitonclick()
