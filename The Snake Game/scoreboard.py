from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}",  align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",  align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
