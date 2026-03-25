import turtle
import random

SKY = "#1a1a2e"
CITY = "#2d2b55"
CITY2 = "#252344"
WINDOW = "#f0c060"
MOON = "#e8d5a3"
STAR = "#c8c8d0"


def draw_rect(x, y, width, height, color):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_triangle(x1, y1, x2, y2, x3, y3, color):
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


def draw_circle(cx, cy, radius, color):
    turtle.up()
    turtle.goto(cx, cy - radius)
    turtle.down()
    turtle.fillcolor(color)
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_window(x, y, w, h):
    if random.random() > 0.3:
        draw_rect(x, y, w, h, WINDOW)
    else:
        draw_rect(x, y, w, h, CITY)


def draw_windows_grid(bx, by, bw, bh, margin=5):
    cell_w = 8
    cell_h = 10

    cols = (bw - margin) // (cell_w + margin) - 1
    rows = (bh - margin) // (cell_h + margin)

    spacing = (bw - cols * cell_w) // (cols + 1)

    for row in range(rows):
        for col in range(cols):
            wx = bx + spacing + col * (cell_w + spacing)
            wy = by + margin + row * (cell_h + margin)
            draw_window(wx, wy, cell_w, cell_h)


def draw_sky(width, height):
    draw_rect(-width // 2, -height // 2, width, height, SKY)


def draw_stars(count=120):
    for _ in range(count):
        x = random.randint(-380, 380)
        y = random.randint(20, 280)
        size = random.choice([1, 1, 1, 2, 2, 3])
        draw_circle(x, y, size, STAR)


def draw_moon(cx, cy, radius):
    draw_circle(cx, cy, radius, MOON)
    draw_circle(cx + radius // 2, cy + radius // 4, int(radius * 0.85), SKY)


def draw_building(x, y, width, height, color, roof="flat"):
    draw_rect(x, y, width, height, color)
    if roof == "triangle":
        draw_triangle(x, y + height,
                      x + width // 2, y + height + 40,
                      x + width, y + height, color)
    elif roof == "spike":
        draw_triangle(x + width // 4, y + height,
                      x + width // 2, y + height + 60,
                      x + width * 3 // 4, y + height, color)
    elif roof == "tower":
        tw = width // 3
        draw_rect(x + width // 2 - tw // 2, y + height, tw, 30, color)
        draw_triangle(x + width // 2 - tw // 2, y + height + 30,
                      x + width // 2, y + height + 60,
                      x + width // 2 + tw // 2, y + height + 30, color)
    draw_windows_grid(x, y, width, height)


def draw_cityscape():
    buildings = [
        (-400, -300, 90,  280, CITY2, "triangle"),
        (-320, -300, 70,  200, CITY, "flat"),
        (-260, -300, 110, 320, CITY2, "tower"),
        (-160, -300, 80,  240, CITY, "flat"),
        ( -90, -300, 60,  180, CITY2, "spike"),
        ( -40, -300, 100, 360, CITY, "triangle"),
        (  50, -300, 50,  200, CITY2, "spike"),
        (  90, -300, 120, 290, CITY, "tower"),
        ( 200, -300, 80,  250, CITY2, "flat"),
        ( 270, -300, 90,  310, CITY, "triangle"),
        ( 350, -300, 70,  220, CITY2, "tower"),
        (-380, -300, 60,  150, CITY, "flat"),
        ( 410, -300, 60,  190, CITY, "spike"),
    ]
    for b in buildings:
        draw_building(*b)


def draw_foreground():
    buildings_front = [
        (-400, -300, 100, 160, CITY2, "flat"),
        (-310, -300, 80,  130, CITY, "triangle"),
        (-240, -300, 90,  150, CITY2, "flat"),
        (-160, -300, 70,  120, CITY, "spike"),
        ( -95, -300, 110, 170, CITY2, "flat"),
        (   5, -300, 80,  140, CITY, "tower"),
        (  75, -300, 100, 160, CITY2, "flat"),
        ( 165, -300, 70,  130, CITY, "triangle"),
        ( 225, -300, 90,  150, CITY2, "flat"),
        ( 305, -300, 80,  140, CITY, "spike"),
        ( 375, -300, 80,  120, CITY, "flat"),
    ]
    for b in buildings_front:
        draw_building(*b)
    draw_rect(-400, -300, 800, 60, CITY2)


def draw_scene():
    draw_sky(800, 600)
    draw_stars(150)
    draw_moon(-80, 220, 35)
    draw_cityscape()
    draw_foreground()


screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor(SKY)
screen.title("Ночной городской пейзаж")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()

draw_scene()

screen.update()
turtle.done()