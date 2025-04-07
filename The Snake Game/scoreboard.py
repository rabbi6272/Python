from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Ariel", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Get the directory where the script is located
        self.data_file_path = os.path.join(os.path.dirname(__file__), "data.txt")
        
        try:
            with open(self.data_file_path, mode="r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            # Create the file with initial high score of 0
            with open(self.data_file_path, mode="w") as file:
                file.write("0")
            self.high_score = 0
        
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}",  align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def end_game(self):
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.hideturtle()
        self.write("GAME OVER",  align=ALIGNMENT, font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
            with open(self.data_file_path, mode="w") as file:
                file.write(f"{self.high_score}")
