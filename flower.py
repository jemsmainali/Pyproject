from turtle import *
import colorsys

speed(0)
bgcolor("black")
hideturtle()

h = 0.0

for i in range(16):
    for j in range(18):
        r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
        color(r, g, b)

        h += 0.005
        if h > 1:
            h = 0

        rt(90)
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)

        circle(40, 24)

done()
