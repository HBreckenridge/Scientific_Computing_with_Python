# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(10, 3)
print(rect.get_area())
print(rect.get_picture())
rect2 = shape_calculator.Rectangle(3,3)
print(rect2.get_area())
print(rect2.get_picture())
print(rect.get_amount_inside(rect2))
sq = shape_calculator.Square(5)
print(sq.get_area())
print(sq.get_amount_inside(rect))
print(sq)
sq.set_side(2)
#print(sq.get_picture())

print(sq.get_picture())
# Run unit tests automatically
#main(module='test_module', exit=False)