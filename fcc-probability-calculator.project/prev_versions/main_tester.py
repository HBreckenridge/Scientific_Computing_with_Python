# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from prob_calculator import Hat
from prob_calculator import experiment
from unittest import main

#hat = prob_calculator.Hat(blue=4, red=2, green=6)

#hat = prob_calculator.Hat(blue=3,red=2,green=6)
#probability = prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
#print(probability)
#print(hat.draw(3))
#expected = 0.272
#hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
#probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=1000)
#print(probability)
#expected = 1.0
#self.assertAlmostEqual(actual, expected, delta = 0.01, msg = 'Expected experiment method to return a different probability.')

hat = prob_calculator.Hat(red=5,blue=2)
#print(hat.contents)
actual = hat.draw(2)
actual = hat.draw(2)
#expected = ['blue', 'red']
actual = len(hat.contents)

expected = 5


print(expected)
print(actual)