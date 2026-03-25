import turtle

L = "lightblue"
M = "skyblue"
D = "steelblue"


def triangle(x1, y1, x2, y2, x3, y3, color):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.down()
    turtle.fillcolor(color)
    turtle.pencolor("white")
    turtle.pensize(2)
    turtle.begin_fill()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)
    turtle.end_fill()


def draw_tile(x, y, size, color1, color2, direction):
    if direction == "\\":
        triangle(x, y, x + size, y, x, y - size, color1)
        triangle(x + size, y, x + size, y - size, x, y - size, color2)
    else:
        triangle(x, y, x + size, y, x + size, y - size, color1)
        triangle(x, y, x, y - size, x + size, y - size, color2)


def draw_pattern():
    size = 60
    start_x = -180
    start_y = 180

    pattern = [
        [("//", D, M), ("//", M, D), ("//", L, M),
         ("\\", L, M), ("\\", M, D), ("\\", D, M)],
        [("//", M, L), ("//", D, M), ("//", M, D),
         ("\\", M, D), ("\\", D, M), ("\\", M, L)],
        [("//", L, M), ("//", M, L), ("//", D, M),
         ("\\", D, M), ("\\", M, L), ("\\", L, M)],
        [("\\", M, L), ("\\", L, M), ("\\", M, D),
         ("//", M, D), ("//", L, M), ("//", M, L)],
        [("\\", L, M), ("\\", M, D), ("\\", D, M),
         ("//", D, M), ("//", M, D), ("//", L, M)],
        [("\\", M, D), ("\\", D, M), ("\\", M, L),
         ("//", M, L), ("//", D, M), ("//", M, D)],
    ]

    for row in range(6):
        for col in range(6):
            x = start_x + col * size
            y = start_y - row * size
            direction, color1, color2 = pattern[row][col]
            draw_tile(x, y, size, color1, color2, direction)


turtle.speed(0)
turtle.hideturtle()
draw_pattern()
turtle.done()