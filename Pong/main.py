from turtle import Turtle,Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Decor
decor = Turtle()
decor.speed("fastest")
decor.hideturtle()
decor.color("white")
decor .goto(0,-100)
decor.circle(100)
decor.penup()
decor.goto(0,0)
decor.pendown()
decor.goto(0,300)
decor.goto(0,-300)
screen = Screen()
screen.setup(width=800 , height= 600)
screen.bgcolor("black")
screen.title('pong')
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()
screen.listen()
screen.onkey(key = "Up", fun = r_paddle.go_up)
screen.onkey(key = "Down", fun = r_paddle.go_down)
screen.onkey(key = "w", fun = l_paddle.go_up)
screen.onkey(key = "s", fun = l_paddle.go_down)

game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()
    if ball.distance(r_paddle)<40 and ball.xcor()>320 or ball.distance(l_paddle)<40 and ball.xcor()<-320 :
        ball.collide()
    if ball.xcor()>375:
        ball.refresh()
        score.update_l()

    if ball.xcor()<-375:
        ball.refresh()
        score.update_r()


    if score.l_score == 10 or score.r_score == 10:
        ball.refresh()
        screen.update()
        game = False

    ball.move()






screen.exitonclick()