import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)
turtle = turtle_module.Turtle()
turtle.speed(0)
turtle.penup()
turtle.hideturtle()


rgb_colors = []
colors = colorgram.extract('image.jpg', 14)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

# color_list = [(243, 233, 207), (58, 91, 120), (208, 224, 211), (26, 56, 86), (170, 161, 145), (37, 64, 96),
#               (211, 196, 163), (139, 159, 169), (118, 116, 110), (160, 176, 169), (200, 215, 220), (178, 200, 189),
#               (95, 107, 103), (102, 89, 99), (130, 129, 121), (110, 126, 150), (97, 137, 152), (161, 151, 156),
#               (233, 179, 155), (174, 199, 203), (227, 220, 224), (32, 72, 91), (33, 33, 20), (117, 133, 129),
#               (29, 39, 32), (183, 190, 204), (138, 121, 126), (143, 120, 116), (52, 70, 66), (71, 58, 72), (61, 52, 61),
#               (200, 186, 191), (68, 67, 53), (72, 60, 59)]

# turtle.setheading(225)
# turtle.forward(300)
# turtle.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     turtle.dot(20, random.choice(color_list))
#     turtle.forward(50)
#
#     if dot_count % 10 == 0:
#         turtle.setheading(90)
#         turtle.forward(50)
#         turtle.setheading(180)
#         turtle.forward(500)
#         turtle.setheading(0)
















screen = turtle_module.Screen()
screen.exitonclick()