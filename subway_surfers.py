import random
import turtle
import time

sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("black")
sc.setup(width=1000, height=600)

obstacle_left = turtle.Turtle()
obstacle_left.speed(40)
obstacle_left.shape("square")
obstacle_left.color("red")
obstacle_left.penup()
obstacle_left.goto(150, 200)

obstacle_middle = turtle.Turtle()
obstacle_middle.speed(40)
obstacle_middle.shape("square")
obstacle_middle.color("red")
obstacle_middle.penup()
obstacle_middle.goto(0, 200)

obstacle_left_middle = turtle.Turtle()
obstacle_left_middle.speed(40)
obstacle_left_middle.shape("square")
obstacle_left_middle.color("red")
obstacle_left_middle.penup()
obstacle_left_middle.goto(75, 200)

obstacle_right_middle = turtle.Turtle()
obstacle_right_middle.speed(40)
obstacle_right_middle.shape("square")
obstacle_right_middle.color("red")
obstacle_right_middle.penup()
obstacle_right_middle.goto(-75, 200)

obstacle_right = turtle.Turtle()
obstacle_right.speed(40)
obstacle_right.shape("square")
obstacle_right.color("red")
obstacle_right.penup()
obstacle_right.goto(-150, 200)

coin_left = turtle.Turtle()
coin_left.speed(40)
coin_left.shape("circle")
coin_left.color("green")
coin_left.penup()
coin_left.goto(150, 200)

coin_middle = turtle.Turtle()
coin_middle.speed(40)
coin_middle.shape("circle")
coin_middle.color("green")
coin_middle.penup()
coin_middle.goto(0,0)

coin_right = turtle.Turtle()
coin_right.speed(40)
coin_right.shape("circle")
coin_right.color("green")
coin_right.penup()
coin_right.goto(-150, 200)

Hero = turtle.Turtle()
Hero.speed(40)
Hero.shape("square")
Hero.color("blue")
Hero.penup()
Hero.goto(0, -100)

# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("White")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Score : 0", align="center", font=("Bubblegum.ttf", 24, "normal"))


def moveleft():
    x = Hero.xcor()
    if x != -150:
        Hero.setx(x-75)

def moveright():
    x = Hero.xcor()
    if x != 150:
        Hero.setx(x+75)


def get_far(num):
    prob = [3, 4, 5, 6, 7, 8, 9,3, 4, 5, 6, 7, 8, 9,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 10 , 14, 15, 16]
    if num == 1:
        x = random.uniform(15,20) if random.uniform(0,3)<1 else random.uniform(5,9)
    else :
        x = random.choice(prob)
    return x


def check_colloision(obs):
    HeroX = Hero.xcor()
    obsY = obs.ycor()
    obsX = obs.xcor()

    if HeroX == obsX and -80>obsY>-120:
        score_display('game_over')
        time.sleep(10)
        return True
    return False



def update_position():

    obstacle_left.sety(obstacle_left.ycor() - get_far(0) - random.uniform(5,7))
    obstacle_left_middle.sety(obstacle_left_middle.ycor() - get_far(0) + random.uniform(2,5))
    obstacle_middle.sety(obstacle_middle.ycor() - get_far(0))
    obstacle_right_middle.sety(obstacle_right_middle.ycor() - get_far(0) + random.uniform(2,7))
    obstacle_right.sety(obstacle_right.ycor() - get_far(0) + random.uniform(2,5))


    if obstacle_left.ycor() < -200:  # Adjust as needed
        obstacle_left.sety(200)
    if obstacle_left_middle.ycor() < -200:  # Adjust as needed
        obstacle_left_middle.sety(200)
    if obstacle_middle.ycor() < -200:  # Adjust as needed
        obstacle_middle.sety(200)
    if obstacle_right_middle.ycor() < -200:  # Adjust as needed
        obstacle_right_middle.sety(200)
    if obstacle_right.ycor() < -200:  # Adjust as needed
        obstacle_right.sety(200)


    coin_left.sety(coin_left.ycor() - get_far(0) + random.uniform(2,7))
    coin_middle.sety(coin_middle.ycor() - get_far(0))
    coin_right.sety(coin_right.ycor() - get_far(0) - random.uniform(2,5))


    if coin_left.ycor() < -200:  # Adjust as needed
        coin_left.sety(200)
    if coin_middle.ycor() < -200:  # Adjust as needed
        coin_middle.sety(200)
    if coin_right.ycor() < -200:  # Adjust as needed
        coin_right.sety(200)


def score_display(score):
    sketch.clear()
    sketch.write(
        f"Score : {score}", align="center", font=("Bubblegum.ttf", 24, "normal")
    )


# Listen for keypresses
sc.listen()
sc.onkey(moveleft, "Left")  # Changed to "Left"
sc.onkey(moveright, "Right")  # Changed to "Right"
start_time = time.time()
while True:
    sc.update()
    update_position()
    score_display(int((time.time() - start_time) * 10))
    if check_colloision(obstacle_left) or check_colloision(obstacle_middle) or check_colloision(obstacle_right_middle) or check_colloision(obstacle_right) or check_colloision(obstacle_left_middle):
        break


