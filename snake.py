from turtle import Turtle, turtles

class Snake:
    def __init__(self):
        self.turtules=[]
        self.position=[(-40,0),(-20,0),(0,0)]
        self.creat_snake()
        self.head=self.turtules[-1]

    def creat_snake(self):
        for i in range(len(self.position)):
            new_trtule=Turtle("square")
            new_trtule.color("white")
            new_trtule.penup()
            new_trtule.goto(self.position[i])
            self.turtules.append(new_trtule)
    def move(self):
        for i in range(len(self.turtules)-1):
            self.turtules[i].goto(self.turtules[i+1].pos())
        self.turtules[-1].forward(10)
        
    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)
    
    def extend(self):
        new_square=Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(self.turtules[0].pos())
        self.turtules.insert(0,new_square)