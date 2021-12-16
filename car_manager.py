from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_y = random.randint(-250, 250)
        new_car.sety(new_y)
        new_car.setx(320)
        self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            new_x = car.xcor() - self.car_speed
            car.setx(new_x)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT

    def start_again(self):
        for car in self.car_list:
            car.reset()
            car.penup()
            car.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
