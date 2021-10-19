from turtle import Turtle, register_shape
import random
from bullet import Bullet

STEP = 10
ROW_LENGTH = 5
ROW_NUMBER = 3

register_shape("invader_one (1).gif")
register_shape("invader_two (1).gif")


class InvaderManager:

    def __init__(self, width):
        self.bullets = []
        self.all_invaders = []
        self.all_invaders_left = []
        self.width = width
        self.left = True
        invader = True
        for i in range(ROW_NUMBER):
            invader = not invader
            for j in range(ROW_LENGTH):
                self.create_invader((-150 + (80 * j), 250 - (100 * i)), invader)

    def create_invader(self, position, type):
        invader = Turtle()
        if type:
            invader.shape("invader_one (1).gif")
        else:
            invader.shape("invader_two (1).gif")
        invader.pu()
        invader.goto(position)
        self.all_invaders.append(invader)
        self.all_invaders_left.append(invader)

    def move_invaders(self):
        if self.left:
            if self.all_invaders_left[0].xcor() < -(self.width / 2) + 50:
                self.left = False
            else:
                for invader in self.all_invaders_left:
                    invader.backward(STEP)
        else:
            if self.all_invaders_left[-1].xcor() > (self.width/2) - 50:
                self.left = True
            else:
                for invader in self.all_invaders_left:
                    invader.forward(STEP)

    def remove_invader(self, invader):
        invader.reset()
        invader.ht()
        self.all_invaders[self.all_invaders.index(invader)] = None
        self.all_invaders_left.remove(invader)

    def in_front_row(self, invader):
        index = self.all_invaders.index(invader)
        if index + ROW_LENGTH > len(self.all_invaders) - 1:
            return True
        if index + (ROW_LENGTH * 2) > len(self.all_invaders) - 1:
            if not self.all_invaders[index + ROW_LENGTH]:
                return True
        if not self.all_invaders[index + ROW_LENGTH] and not self.all_invaders[index + (ROW_LENGTH * 2)]:
            return True
        return False

    def more_invaders(self):
        return len(self.all_invaders_left) > 0

    def shoot(self):
        shoot = random.randint(1, 10)
        if shoot == 1:
            invader = random.choice(self.all_invaders_left)
            if self.in_front_row(invader):
                bullet = Bullet(False, (invader.xcor(), invader.ycor() - 10))
                self.bullets.append(bullet)
