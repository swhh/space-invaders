from turtle import Screen
from cannon import Cannon
from invadermanager import InvaderManager
from scoreboard import ScoreBoard
from obstaclemanager import ObstacleManager
import time

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 600
BG_COLOR = 'black'
START_POSITION = (0, -SCREEN_HEIGHT / 2 + 100)


screen = Screen()
screen.bgcolor(BG_COLOR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Space Invaders")
screen.tracer(0)
player = Cannon(START_POSITION)
invaders = InvaderManager(SCREEN_WIDTH)
obstacles = ObstacleManager(SCREEN_WIDTH)


score = ScoreBoard(SCREEN_WIDTH, SCREEN_HEIGHT)


screen.update()
screen.listen()
screen.onkey(player.right, 'Right')
screen.onkey(player.left, 'Left')
screen.onkey(player.shoot, 'space')

game_is_on = True
blocks_to_remove = set()
bullets_to_remove = set()
while game_is_on:
    time.sleep(0.05)
    screen.update()
    for bullet in player.bullets:
        hits = [bullet.distance(invader) < 20 for invader in invaders.all_invaders_left]
        if any(hits):
            invader = invaders.all_invaders_left[hits.index(True)]
            invaders.remove_invader(invader)
            bullets_to_remove.add(bullet)
            score.update_score()
            continue
        hits = [bullet.distance(obstacle) < 20 for obstacle in obstacles.all_obstacles]
        if any(hits):
            obstacle = obstacles.all_obstacles[hits.index(True)]
            obstacles.remove_obstacle(obstacle)
            bullets_to_remove.add(bullet)
            continue
        if bullet.out_of_screen(SCREEN_HEIGHT):
            bullet.remove_bullet()
            bullets_to_remove.add(bullet)
            continue
        bullet.fire()
    if bullets_to_remove:
        for bullet in bullets_to_remove:
            bullet.remove_bullet()
            player.bullets.remove(bullet)
        bullets_to_remove.clear()
    for bullet in invaders.bullets:
        if bullet.distance(player) < 20:
            if score.lives > 0:
                score.lives -= 1
                score.update_score()
                bullets_to_remove.add(bullet)
                break
            else:
                score.game_over()
                break
        hits = [bullet.distance(obstacle) < 20 for obstacle in obstacles.all_obstacles]
        if any(hits):
            obstacle = obstacles.all_obstacles[hits.index(True)]
            obstacles.remove_obstacle(obstacle)
            bullets_to_remove.add(bullet)
            continue
        if bullet.out_of_screen(SCREEN_HEIGHT):
            bullet.remove_bullet()
            bullets_to_remove.add(bullet)
            continue
        bullet.fire()
    if bullets_to_remove:
        for bullet in bullets_to_remove:
            bullet.remove_bullet()
            invaders.bullets.remove(bullet)
        bullets_to_remove.clear()
    if not invaders.more_invaders():
        score.game_over(True)
    if score.is_game_over:
        break

    invaders.shoot()
    invaders.move_invaders()

screen.exitonclick()