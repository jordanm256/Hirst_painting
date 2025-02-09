#This program extracts the colors (RGB values) out of an image and creates an almost similar Hirst painting with the extracted colors.

#import colorgram
import random
import turtle as t

"""The program commented out below extracts colors from "hirstdotimage.jpg"
    It then places them as a list of tuples into 'new_colors' and prints them to the console """

# colors = colorgram.extract("hirstdotimage.jpg", 30)


# new_colors = []
# for item in range(len(colors)):
#     first_color = colors[item]
#     r = first_color.rgb[0]
#     g = first_color.rgb[1]
#     b = first_color.rgb[2]
#     rgb_colors = (r, g, b)
#     new_colors.append(rgb_colors)
#
# print(new_colors)

"""The list of tuples is copied from console and placed into 'hirst_colors'. 
    Be sure to run the color extraction program before the rest."""

hirst_colors = [(29, 41, 60), (49, 92, 143), (145, 81, 44), (170, 14, 28), (160, 56, 87), (227, 154, 8),
                (209, 162, 105), (235, 217, 75), (66, 30, 43), (37, 142, 47), (222, 225, 4), (48, 36, 30), (46, 47, 96), (95, 193, 168), (120, 161, 172), (19, 54, 47), (243, 89, 22), (161, 16, 13),
                (18, 97, 45), (212, 58, 79), (49, 169, 80), (189, 146, 159), (231, 173, 186), (226, 177, 168), (45, 153, 195), (160, 212, 184)]

t.colormode(255) #change color mode of the turtle module so that you can use the tuples as rgb values.
tim = t.Turtle()
tim.speed("fastest")

"""moves turtle to a suitable position on the screen to start movement"""

tim.setheading(225) #moves turtle to a suitable position on the screen to start movement
tim.penup()
tim.hideturtle()
tim.forward(360)
tim.setheading(360)
num_of_dots = 100 #number of dots in the Hirst dot painting.

"""The for loop below takes account of how many dots to draw on the screen and draws until they are complete"""
"""Each row has a total of 10 dots, once ten is reached the turtle changes direction,
    moves upwards and then to the left until it reaches the start of the line. Then the drawing process is repeated"""
for dots in range(1,num_of_dots + 1): #The last dot is not drawn, we add 1 to account for it.
    tim.dot(20,random.choice(hirst_colors))
    tim.penup()
    tim.forward(60)
    tim.penup()

    if dots % 10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(60)
        tim.setheading(180)
        tim.penup()
        tim.forward(600)
        tim.setheading(0)





print(tim.position())





screen = t.Screen()
screen.exitonclick()
