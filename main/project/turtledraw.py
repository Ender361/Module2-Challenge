# Author: Justin Wheeler
# Date: 4/30/2021
# Draws A program to draw many different overlapping sqaures at different angles

# Importing the turtle module and setting turtle so it draws instantly
import turtle
t = turtle.Turtle()
t.speed(0)
turtle.tracer(0, 0)

# Using a for loop to create the pattern at 4 different spots
for x in range(-200, 201, 400):
    for y in range(-200, 201, 400):
        t.up()
        t.goto(x,y)
        t.down()
        # Adding color to each pattern
        if x > 0 and y > 0:
            t.pencolor("#33FDFF")
        elif x > 0 and y < 0:
            t.pencolor("#53FF33")
        elif x < 0 and y > 0:
            t.pencolor("#FF6433")
        else:
            t.pencolor("#FF33E6")
        for i in range(60):
            for r in range(4):
                t.fd(100)
                
                t.left(90)
            t.left(6)
        
turtle.update()
