from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.7,0.7)
        self.color('blue')
        self.speed('fastest')
        
    

    def refresh(self):
        self.random_x=random.randint(-270,270)
        self.random_y=random.randint(-270,270)
        self.goto(self.random_x,self.random_y)
