# Import required library
import random
import turtle

# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("black")
sc.setup(width=1000, height=600)


# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)


# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)


# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("white")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = random.uniform(-5, -2) if random.choice([True, False]) else random.uniform(2, 5)
hit_ball.dy = random.uniform(-5,5)

left_player = 0
right_player = 0

font_type = 'Bubblegum.ttf'

# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("White")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",align="center", font=("Bubblegum.ttf", 24, "normal"))


def paddleaup(speed):
    y = left_pad.ycor()
    if(y < 250):
        y+= speed
        left_pad.sety(y)


def paddleadown(speed):
    y = left_pad.ycor()
    if(y>-250):
        y -= speed
        left_pad.sety(y)


def paddlebup(speed):
    y = right_pad.ycor()
    if(y<250):
        y += speed
        right_pad.sety(y)


def paddlebdown(speed):
    y = right_pad.ycor()
    if(y>-250):
        y -= speed
        right_pad.sety(y)

speed = 20

# Keyboard bindings
sc.listen()
sc.onkeypress(lambda: paddleaup(speed), "e")
sc.onkeypress(lambda: paddleadown(speed), "x")
sc.onkeypress(lambda: paddlebup(speed), "Up")
sc.onkeypress(lambda: paddlebdown(speed), "Down")

color_names = [
    "AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure",
    "Beige", "Bisque", "Black", "BlanchedAlmond", "Blue",
    "BlueViolet", "Brown", "BurlyWood", "CadetBlue", "Chartreuse",
    "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson",
    "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenrod", "DarkGray",
    "DarkGreen", "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange",
    "DarkOrchid", "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue",
    "DarkSlateGray", "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue",
    "DimGray", "DodgerBlue", "Firebrick", "FloralWhite", "ForestGreen",
    "Fuchsia", "Gainsboro", "GhostWhite", "Gold", "Goldenrod",
    "Gray", "Green", "GreenYellow", "Honeydew", "HotPink",
    "IndianRed", "Indigo", "Ivory", "Khaki", "Lavender",
    "LavenderBlush", "LawnGreen", "LemonChiffon", "LightBlue", "LightCoral",
    "LightCyan", "LightGoldenrodYellow", "LightGray", "LightGreen", "LightPink",
    "LightSalmon", "LightSeaGreen", "LightSkyBlue", "LightSlateGray", "LightSteelBlue",
    "LightYellow", "Lime", "LimeGreen", "Linen", "Magenta",
    "Maroon", "MediumAquamarine", "MediumBlue", "MediumOrchid", "MediumPurple",
    "MediumSeaGreen", "MediumSlateBlue", "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed",
    "MidnightBlue", "MintCream", "MistyRose", "Moccasin", "NavajoWhite",
    "Navy", "OldLace", "Olive", "OliveDrab", "Orange",
    "OrangeRed", "Orchid", "PaleGoldenrod", "PaleGreen", "PaleTurquoise",
    "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink",
    "Plum", "PowderBlue", "Purple", "Red", "RosyBrown",
    "RoyalBlue", "SaddleBrown", "Salmon", "SandyBrown", "SeaGreen",
    "SeaShell", "Sienna", "Silver", "SkyBlue", "SlateBlue",
    "SlateGray", "Snow", "SpringGreen", "SteelBlue", "Tan",
    "Teal", "Thistle", "Tomato", "Turquoise", "Violet",
    "Wheat", "White", "WhiteSmoke", "Yellow", "YellowGreen"
]


while True:
    sc.update()

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dx = random.uniform(-5, -2) if random.choice([True, False]) else random.uniform(2, 5)
        hit_ball.dy = random.uniform(-5, 5)
        left_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(left_player, right_player), align="center",font=(font_type, 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dx = random.uniform(-5, -2) if random.choice([True, False]) else random.uniform(2, 5)
        hit_ball.dy = random.uniform(-5, 5)
        right_player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(left_player, right_player), align="center",font=(font_type, 24, "normal"))

    # Paddle ball collision
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 380) and (hit_ball.ycor() < right_pad.ycor() + 60 and hit_ball.ycor() > right_pad.ycor() - 60):
        for i in range(30):
            sc.bgcolor(random.choice(color_names))
        sc.bgcolor("black")
        hit_ball.color(random.choice(color_names))
        hit_ball.setx(360)
        hit_ball.dx = -(hit_ball.dx + 0.25)
        if(hit_ball.dy<0):
            hit_ball.dy = hit_ball.dy - 0.25

    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -380) and (hit_ball.ycor() < left_pad.ycor() + 60 and hit_ball.ycor() > left_pad.ycor() - 60):
        for i in range(30):
            sc.bgcolor(random.choice(color_names))
        sc.bgcolor("black")
        hit_ball.color(random.choice(color_names))
        hit_ball.setx(-360)
        hit_ball.dx = -(hit_ball.dx - 0.25)
        if (hit_ball.dy < 0):
            hit_ball.dy = hit_ball.dy - 0.25
        else:
            hit_ball.dy = hit_ball.dy + 0.25

