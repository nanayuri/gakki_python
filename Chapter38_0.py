import math as m


class Point:
    def __init__(self):
        self.x1 = float(input("请输入第一个点的横坐标:"))
        self.y1 = float(input("请输入第一个点的纵坐标:"))
        self.x2 = float(input("请输入第二个点的横坐标:"))
        self.y2 = float(input("请输入第二个点的纵坐标:"))


class Line(Point):
    def __init__(self):
        super().__init__()

    def getLen(self):
        length = m.sqrt(((self.x1 - self.x2) * (self.x1 - self.x2)) + ((self.y1 - self.y2) * (self.y1 - self.y2)))
        print(length)


line = Line()
line.getLen()
