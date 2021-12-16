from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.color("black")
        self.write(f"Level: {self.player_score}", font=FONT)

    def next_level(self):
        self.clear()
        self.player_score += 1
        self.write(f"Level: {self.player_score}", font=FONT)

    def game_over(self):
        # self.clear()
        self.goto(0, 0)
        self.write("Game Over!\nPress 'y' to restart\nor 'n' to Quit!", font=FONT, align="center")

    def start_again(self):
        self.clear()
        self.player_score = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.color("black")
        self.write(f"Level: {self.player_score}", font=FONT)




