from turtle import Turtle

NUMBER_OF_BLOCKS = 4
CLUSTER_SIZE = 5


class ObstacleManager:
    def __init__(self, width):
        self.all_obstacles = []
        gap = (width / NUMBER_OF_BLOCKS)
        for i in range(NUMBER_OF_BLOCKS):
            start_position = (-width/2 + 30 + gap*i, -100)
            for j in range(CLUSTER_SIZE):
                for k in range(CLUSTER_SIZE):
                    self.create_obstacle((start_position[0] + 20*j, start_position[1] + 20*k))

    def create_obstacle(self, position):
        obstacle = Turtle()
        obstacle.shape("square")
        obstacle.color("white")
        obstacle.pu()
        obstacle.goto(position)

        self.all_obstacles.append(obstacle)

    def remove_obstacle(self, obstacle):
        obstacle.reset()
        self.all_obstacles.remove(obstacle)



