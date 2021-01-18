import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
cars = CarManager()
screen.listen()
screen.onkey(key= "Up", fun= player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    if player.refresh() == True:
        score.update()
        cars.speed_up()
    for car in cars.all_cars:
        if car.distance(player)<26:
            game_is_on = False
            score.game_over()

screen.exitonclick()



