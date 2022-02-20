from turtle import Turtle
FONT = ('Courier', 23, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.high_score = 0
        self.penup()
        self.pencolor("white")
        self.setposition(0, 270)
        self.hideturtle()
        self.fillcolor("white")

    def increase_player_score(self):
        self.player_score += 1

    def print_scoreboard(self):
        self.clear()  # removes the previous scoreboard from screen to prevent overlays
        self.write(f"Score:{self.player_score}   HighScore:{self.high_score}", False, align="center", font=FONT)

    def reset(self):
        if self.player_score > self.high_score:
            self.high_score = self.player_score
        self.player_score = 0
        self.print_scoreboard()
