from turtle import Turtle, register_shape
from bullet import Bullet

WEST = 180
STEP = 10

register_shape("cannon (1).gif")


class Cannon(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('cannon (1).gif')
        self.pu()
        self.goto(position)
        self.bullets = []

    def left(self):
        self.backward(STEP)

    def right(self):
        self.forward(STEP)

    def shoot(self):
        bullet = Bullet(True, (self.xcor(), self.ycor() + 10))
        self.bullets.append(bullet)
