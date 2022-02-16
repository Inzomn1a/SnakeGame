from snake import Snake
from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard

# Setup SnakeGame Viewport
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
# Getting player input
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# GAME LOOP
game_is_on = True
while game_is_on:
    scoreboard.print_scoreboard()
    snake.move()
    time.sleep(0.075)  # Updates per second / Speed of snake
    screen.update()

    # Detect foodCollision //respawn food and increase score on hit
    if snake.snakehead.distance(food) < 16:  # size of hitbox
        snake.extend_snake()
        food.food_respawn()
        scoreboard.increase_player_score()

    # Detect wallCollision
    if snake.snakehead.xcor() > 280 or snake.snakehead.xcor() < -300 or snake.snakehead.ycor() > 300 or snake.snakehead.ycor() < -280:
        game_is_on = False
        screen.bgcolor("red")
        scoreboard.game_over_sequence()

    # Detect tailCollision
    for segment in snake.segments[1:]:
        if snake.snakehead.distance(segment) < 10:
            game_is_on = False
            screen.bgcolor("red")
            scoreboard.game_over_sequence()


screen.exitonclick()
