import copy
import random
from random import choice
# Consider using the modules imported above.

class Hat:
    contents = []
    def __init__(self, **types_of_balls):
        for balls in types_of_balls:
            self.balls = types_of_balls
        for ball in types_of_balls:
            for i in range(self.balls[ball]):
                self.contents.append(ball)
    
    def draw(self, num_balls_drawn = 1):
        balls = self.balls
        picked_balls = {}
        for M in range(num_balls_drawn):

            picked_ball = choice(list(balls))
            
            try:
                picked_balls[picked_ball] += 1
            except KeyError:
                picked_balls[picked_ball] = 1
        return picked_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat = hat

    def pick_from_hat(expected_balls, num_balls_drawn):
        drawn_balls = hat.draw(num_balls_drawn)
        x = drawn_balls
        y = expected_balls
        shared_items = {k: x[k] for k in x if k in y and x[k] >= y[k]}
        success = len(expected_balls) == len(shared_items)
        return success

    success = 0
    for i in range(num_experiments):
        success += int(pick_from_hat(expected_balls, num_balls_drawn))
    probability_of_success = success/num_experiments
    returnProbability = '%.3f' % probability_of_success
    return returnProbability