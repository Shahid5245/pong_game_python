from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_bord import ScoreBord
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(titlestring="Famous Pong Game")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
score_bord = ScoreBord()

screen.listen()
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

screen.onkey(key="8", fun=r_paddle.up)
screen.onkey(key="5", fun=r_paddle.down)

is_game_on = True
while is_game_on:

    time.sleep(ball.move_speed)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 400:
        ball.refresh()
        score_bord.l_point()


    if ball.xcor() < - 400:
        ball.refresh()
        score_bord.r_point()


screen.exitonclick()
