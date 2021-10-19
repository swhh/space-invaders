from turtle import Turtle

LIVES = 3


class ScoreBoard(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.player_score = 0
        self.text = "Score: {}\n Lives: {}"
        self.color('white')
        self.pu()
        self.hideturtle()
        self.width = width
        self.height = height
        self.goto(width/2-150, height/2 - 100)
        self.lives = LIVES
        self.write_score()
        self.is_game_over = False

    def write_score(self):
        self.goto(self.width / 2 - 120, self.height / 2 - 120)
        self.write(self.text.format(self.player_score, self.lives), True, align='center', font=('arial', 30, 'normal'))

    def update_score(self):
        self.player_score += 1
        self.clear()
        self.setx(260)
        self.write_score()

    def game_over(self, win=False):
        self.is_game_over = True
        self.goto(0, 0)
        if win:
            self.write("YOU WON!", True, align='center', font=('arial', 34, 'normal'))
        else:
            self.write("GAME OVER!", True, align='center', font=('arial', 34, 'normal'))