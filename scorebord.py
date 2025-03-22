from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score=0
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score: {self.score}   High Score:{self.high_score}",align="center",font=["Arial",24,"normal"])
    
    def increas_score(self):
        self.score +=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.screen.bgcolor("darkred")
        self.goto(0,0)
        if self.score>self.high_score:
            self.high_score=self.score
        self.write(f"--------------Game over--------- \n\nFinal score:{self.score}\n\nHigh Score :{self.high_score}",align="center",font=["Arial",24,"normal"])

        

        



