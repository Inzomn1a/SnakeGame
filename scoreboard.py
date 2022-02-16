from turtle import Turtle
FONT = ('Courier', 23, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.penup()
        self.pencolor("white")
        self.setposition(0, 270)
        self.hideturtle()
        self.fillcolor("white")

    def increase_player_score(self):
        self.player_score += 1

    def print_scoreboard(self):
        self.clear()  # removes the previous scoreboard from screen to prevent overlays
        self.write(f"Score: {self.player_score}", False, align="center", font=FONT)

    def game_over_sequence(self):
        self.goto(0, 0)
        self.write("You Lost.", False, align="center", font=('Courier', 50, 'normal'))