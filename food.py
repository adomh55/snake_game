from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("cyan")
        self.penup()
        self.shapesize(0.5,0.5)
        self.appear()
    def appear(self):
        x_cor=random.randint(-350,350)
        y_cor=random.randint(-350,350)
        self.goto(x_cor,y_cor)

