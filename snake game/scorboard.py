from turtle import  Turtle
ALIGMENT="center"
FONT=("Arial",24,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as file:
            self.highscore=int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(f"score : {self.score},High score:{self.highscore}",align=ALIGMENT,font=FONT)
    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_screen()
    def increase_score(self):
        self.score+=1
        self.update_screen()