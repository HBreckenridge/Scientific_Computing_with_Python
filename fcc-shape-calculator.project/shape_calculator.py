from math import floor
class Rectangle:
    width = 0
    height = 0
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
        
    def set_height(self, height):
        self.height = height

    def get_area(self):
        w = self.width
        h = self.height
        a = w*h
        return a
    
    def get_perimeter(self):
        w = self.width
        h = self.height
        p = 2*(h+w)
        return p
    
    def get_diagonal(self):
        w = self.width
        h = self.height
        c = ((w ** 2 + h ** 2) ** .5)
        diagonal = round(c,3)
        return c

    def get_picture(self):
        w = self.width
        h = self.height
        shape=''
        char = "*"
        if w >= 50 or h >= 50:
            shape = str("Too big for picture.")
        else:
            for i in range(h):
                ystr = (""""""+char*w+"""\n""")
                shape+=str("""{0}""").format(ystr)
        return shape

    def get_amount_inside(self, shape):
        inArea = shape.get_area()
        outArea = self.get_area()
        numInside = floor(outArea/inArea)
        returnString = numInside
        return returnString

    def __str__(self):
        returnString = str(self.__class__.__name__)+"(width="+str(self.width)+", height="+str(self.height)+")"
        return returnString


class Square(Rectangle):
    width = 0
    height = 0
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        returnString = str(self.__class__.__name__)+"("+"side="+str(self.width)+")"
        return returnString

