class Rect:
    def __init__(self, wide = 0, height = 0):
        self.wide = wide
        self.height = height

    def __setattr__(self, name, value):
        if name == 'square':
            self.wide = value
            self.height = value
        else:
            super().__setattr__(name, value)

    def getArea(self):
        return self.wide * self.height