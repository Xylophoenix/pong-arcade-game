from hashlib import new
from turtle import Screen, Turtle
import time
import turtle
from ball import Ball

from paddle import Paddle
from scoreboard import Score
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
score = Score()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -345:
        ball.bounce_x()
        ball.increase_speed()
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_postition()
    if ball.xcor() < -380:
        score.r_point()
        ball.reset_postition()

screen.exitonclick()


