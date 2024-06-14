from turtle import Screen
from snake import Snake
from food import Food
from scorboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect snake and food collision
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #detect for snake and wall colision
    if snake.head.xcor()>298 or snake.head.xcor()<-298 or snake.head.ycor()>298 or snake.head.ycor()<-298:
        scoreboard.reset()
        snake.reset()
    #detect colison with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()