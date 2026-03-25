import turtle

PINK = "salmon"
BLUE = "lightblue"
DARK_BLUE = "navy"


def triangle(x1, y1, x2, y2, x3, y3, color):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()


def square(cx, cy, s, color, border=None):
    turtle.up()
    turtle.goto(cx, cy + s)
    turtle.down()
    turtle.fillcolor(color)
    turtle.pencolor(border if border else color)
    turtle.begin_fill()
    turtle.goto(cx + s, cy)
    turtle.goto(cx, cy - s)
    turtle.goto(cx - s, cy)
    turtle.goto(cx, cy + s)
    turtle.end_fill()


def circle(cx, cy, radius, color):
    turtle.up()
    turtle.goto(cx, cy - radius)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def ornament(cx, cy):
    s = 60

    triangle(cx - 120, cy + 120, cx - 60, cy + 120, cx - 120, cy + 60, PINK)
    triangle(cx + 120, cy + 120, cx + 60, cy + 120, cx + 120, cy + 60, PINK)
    triangle(cx - 120, cy - 120, cx - 60, cy - 120, cx - 120, cy - 60, PINK)
    triangle(cx + 120, cy - 120, cx + 60, cy - 120, cx + 120, cy - 60, PINK)

    triangle(cx - 60, cy + 120, cx, cy + 60, cx + 60, cy + 120, PINK)
    triangle(cx - 60, cy - 120, cx + 60, cy - 120, cx, cy - 60, PINK)
    triangle(cx - 120, cy + 60, cx - 120, cy - 60, cx - 60, cy, PINK)
    triangle(cx + 120, cy + 60, cx + 120, cy - 60, cx + 60, cy, PINK)

    square(cx, cy, s, PINK)

    square(cx - 60, cy + 60, s, BLUE, "navy")
    square(cx + 60, cy + 60, s, BLUE, "navy")
    square(cx - 60, cy - 60, s, BLUE, "navy")
    square(cx + 60, cy - 60, s, BLUE, "navy")


def main():
    turtle.speed(0)
    turtle.hideturtle()
    for i in range(3):
        for j in range(3):
            ornament(-240 + i * 240, -240 + j * 240)
    for i in range(3):
        for j in range(3):
            ox = -240 + i * 240
            oy = -240 + j * 240
            circle(ox - 60, oy, 10, DARK_BLUE)
            circle(ox + 60, oy, 10, DARK_BLUE)
            circle(ox, oy + 60, 10, DARK_BLUE)
            circle(ox, oy - 60, 10, DARK_BLUE)
            circle(ox - 60, oy + 120, 10, DARK_BLUE)
            circle(ox + 60, oy + 120, 10, DARK_BLUE)
            circle(ox + 120, oy + 60, 10, DARK_BLUE)
            circle(ox + 120, oy - 60, 10, DARK_BLUE)
            circle(ox - 120, oy + 60, 10, DARK_BLUE)
            circle(ox - 120, oy - 60, 10, DARK_BLUE)
            circle(ox - 60, oy - 120, 10, DARK_BLUE)
            circle(ox + 60, oy - 120, 10, DARK_BLUE)
    turtle.done()


main()