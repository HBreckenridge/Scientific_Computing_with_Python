import copy
import random
from random import choice, randrange
# Consider using the modules imported above.

class Hat:
   #contents = []
    def __init__(self, **types_of_balls):

        self.contents = []
        for balls in types_of_balls:
            self.balls = types_of_balls
        for ball in types_of_balls:
            for i in range(self.balls[ball]):
                self.contents.append(ball)
    
    def draw(self, num_balls_drawn = 1):
        print(self.contents)
        balls = self.balls
        picked_balls = {}
        draw = []
        hat_contents = balls.copy()
        print(hat_contents)
        for M in range(num_balls_drawn):
            rand = randrange(0, len(self.contents))
            #print(self.contents[rand])
            picked_ball = choice(list(hat_contents))
            print(hat_contents)
            print(hat_contents)
            draw.append(picked_ball)
            print(picked_ball)
            
        return draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat = hat
    expected = []
    for ball in expected_balls:
        for i in range(expected_balls[ball]):
            expected.append(ball)
    def pick_from_hat(expected_balls, num_balls_drawn):
        drawn_balls = hat.draw(num_balls_drawn)
        success = set(drawn_balls).issubset(set(expected_balls)) 
        return success
    int(pick_from_hat(expected_balls, num_balls_drawn))
    success = 0
    for i in range(num_experiments):
        success += int(pick_from_hat(expected_balls, num_balls_drawn))
    probability_of_success = success/num_experiments
    returnProbability = '%.3f' % probability_of_success
    #returnProbability = float(returnProbability)
    return probability_of_success