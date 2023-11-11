import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    # detect collision with car
    for car in car_manager.cars:
        if player.distance(car.pos()) < 20:
            scoreboard.game_over()
            game_is_on = False
            break

    # increase speed
    if player.check_finish():
        car_manager.increase_new_level_speed()
        scoreboard.increase_level()
        scoreboard.show_level()

screen.exitonclick()
