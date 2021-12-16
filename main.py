import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random




screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()

scoreboard = Scoreboard()
screen.onkeypress(player.go_up, "Up")
screen.listen()
game_is_on = True
game_over = False


def start_over():
    scoreboard.start_again()
    player.next_level()
    car.start_again()
    global game_over
    game_over = False


def end_game():
    global game_is_on
    game_is_on = False


while game_is_on:

    time.sleep(0.1)
    # Create Random Cards
    if random.randint(0, 5) == 1:
        car.create_car()

    if not game_over:
        car.move()
    else:
        # Ask if they want to start again
        screen.onkeypress(start_over, "y")
        screen.onkeypress(end_game, "n")
        screen.listen()
    screen.update()
    # When player reaches top of screen
    if player.ycor() > 280:
        player.next_level()
        scoreboard.next_level()
        car.next_level()
    # Checking for collisions with car
    for specific_car in car.car_list:
        if player.distance(specific_car) < 20 or player.distance(specific_car) < 40 and player.ycor() == specific_car.ycor():
            scoreboard.game_over()
            game_over = True

