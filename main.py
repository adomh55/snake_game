from snake import Snake
from turtle import Screen
import time
from food import Food
from scorebord import Score




window=Screen()
window.setup(800,800)
window.bgcolor("black")
window.tracer(0)


snake=Snake()
food=Food()
score=Score()

game_on=True
while game_on:
    snake.move()
    window.update()
    time.sleep(.1)
    window.listen()
    window.onkeypress(snake.up,"Up")
    window.onkeypress(snake.down,"Down")
    window.onkeypress(snake.left,"Left")
    window.onkeypress(snake.right,"Right")
    if snake.head.distance(food) <10:
        food.appear()
        snake.extend()
        score.increas_score()
    if snake.head.xcor()>370 or snake.head.xcor()<-370 or snake.head.ycor()>370 or snake.head.ycor()<-370:
        
        score.game_over()
        game_on=False
    for segmant in snake.turtules[:-1]:
        if snake.head.distance(segmant)<10:
            game_on=False
            score.game_over()

    




window.exitonclick()
