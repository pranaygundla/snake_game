from turtle import Turtle
ALLIGNMENT='center'
FONT=('Arial',15,'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        # self.high_score=0
        with open("data1.txt") as data:
            self.high_score=int(data.read())
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f'Score : {self.score} \t\t High_Score : {self.high_score}',align=ALLIGNMENT,font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open('data1.txt','w') as data:
                data.write(f'{self.high_score}')
        self.update_score_board()
        self.score=0

        
    def increase_score(self):
        self.score+=1
        self.update_score_board()
    
   
    
