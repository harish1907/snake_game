from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.score_box()

    def score_box(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.writer_score()

    def writer_score(self):
        self.write(f"Score: {self.score}", move=True, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.goto(0, 270)
        self.writer_score()
