from turtle import Turtle

STEP = 10


class Bullet(Turtle):

    def __init__(self, cannon, starting_point):
        super().__init__()
        self.cannon = cannon
        self.shape('square')
        self.speed('fast')
        self.turtlesize(stretch_wid=0.1, stretch_len=0.2)
        self.goto(starting_point)
        self.color("white")
        self.pu()
        if self.cannon:
            self.left(90)
        else:
            self.right(90)

    def remove_bullet(self):
        self.reset()
        self.ht()

    def fire(self):
        self.forward(STEP)

    def out_of_screen(self, height):
        if self.cannon:
            return self.ycor() > (height / 2)
        return self.ycor() < -(height / 2) - 20
