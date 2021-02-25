from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0

        self.update_scoreboard()



    def add_score(self):
        self.score += 1




