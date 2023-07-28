import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim.shapesize(3.0, 3.0)
tim.shape("turtle")
tim.color("green")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
directions = [90, 180, 270, 0]


# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)



# for _ in range(15):
#     tim.pendown()
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

# Random Walk

# tim.pensize(10)


# for _ in range(200):
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())
#     tim.forward(25)

# Draw multiple circles
heading = 0
tim.speed(0)

while heading < 360:
    tim.setheading(heading)
    tim.color(random_color())
    tim.circle(100)
    heading += 5

















screen = Screen()
screen.exitonclick()
