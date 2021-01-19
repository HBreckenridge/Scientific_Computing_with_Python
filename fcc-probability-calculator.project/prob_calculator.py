import copy
import random
from random import choice, randrange
# Consider using the modules imported above.

class Hat:
    contents = []
    original_contents = []
    def __init__(self, **types_of_balls):
        self.contents = []
        for balls in types_of_balls:
            self.balls = types_of_balls
        for ball in types_of_balls:
            for i in range(self.balls[ball]):
                self.contents.append(ball)
        
        self.original_contents = self.contents.copy()

    
    def draw(self, num_balls_drawn = 1):
        #print(self.original_contents)
        self.contents = self.original_contents.copy()
        total_balls_in_hat = self.contents
        draw = []
        hat_contents = self.contents
        for M in range(num_balls_drawn):
            try:
                picked_ball = choice(list(hat_contents))
                draw.append(picked_ball)
                hat_contents.remove(picked_ball)

            except IndexError:
                pass
        return draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat = hat
    expected = []
    for ball in expected_balls:
        for i in range(expected_balls[ball]):
            expected.append(ball)

        def pick_from_hat(expected_balls, num_balls_drawn):
            drawn_balls = hat.draw(num_balls_drawn)
            if len(drawn_balls)> len(expected_balls):
                b = expected_balls
                a = drawn_balls
            else:
                b = drawn_balls
                a = expected_balls

            success= all(True if b.count(item) <= a.count(item) else False for item in b)
            return success


    success = 0
    for i in range(num_experiments):
        success += int(pick_from_hat(expected, num_balls_drawn))
    probability_of_success = success/num_experiments

    return probability_of_success