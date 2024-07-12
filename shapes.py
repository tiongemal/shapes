class Quadrilateral:
    def __init__(self, s1, s2, s3, s4):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4

    def __repr__(self):
        return "quadrilateral with side lengths " + \
               str(self.s1) + ", " + str(self.s2) + \
               ", " + str(self.s3) + ", " + str(self.s4)


class Rectangle(Quadrilateral):
    def __init__(self, s1, s2):
        super().__init__(s1, s2, s1, s2)

    def __repr__(self):
        rv = "Rectangle with side lengths " + \
               str(self.s1) + ", " + str(self.s2)
        rv +=  "\nArea: " + str(self.cal_area())
        return rv

    def cal_area(self):
        return self.s1 * self.s2

class Square(Rectangle):
    def __init__(self, s):
        super().__init__(s, s)

    def __repr__(self):
        rv = "\nsquare with side lengths " + \
               str(self.s1)
        rv+=  "\nArea: " + str(self.cal_area())
        return rv

    def cal_area(self):
        return self.s1 * self.s2


class Circle:
    def __init__(self, r):
        self.radius = r

    def __repr__(self):
        rv = "\nCircle with radius " + str(self.radius)
        rv += "\nArea: " + str(self.calc_area())
        return rv

    def calc_area(self):
        return 3.14 * (self.radius **2)


Circ = Circle(5)

print(Circ.calc_area())