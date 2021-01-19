import copy
import random
from random import choice
# Consider using the modules imported above.

class Hat:

    def __init__(self, **types_of_balls):
        for balls in types_of_balls:
            self.balls = types_of_balls
    
    def draw(self):
        balls = self.balls
        i = choice(list(balls))
        current_count = balls[i]
        new_count = balls[i] -1
        balls[i] = new_count
        picked_ball = balls[i]
        if balls[i] <= 0:
            del balls[i]
        self.balls = balls
        return picked_ball, balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    print(hat.balls)
    print(expected_balls)
    print(num_balls_drawn)
    print(num_experiments)
    return