COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1,6)==1:
            car = Turtle()
            car.color(random.choice(COLORS))
            car.shape("square")
            car.penup()
            car.shapesize(stretch_len=2)
            car.setheading(180)
            car.goto(x=300, y=random.randint(-250, 250))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
