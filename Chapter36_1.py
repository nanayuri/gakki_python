class Rectangle:
    length = 5.00
    width = 4.00

    def getRect(self):
        print("这个矩形的长是：%4.2f,宽是:%4.2f" %(self.length, self.width))

    def setRect(self):
        print("请输入矩形的长和宽...")
        self.length = float(input("长："))
        self.width = float(input("宽："))
        print(type(self.length))

    def getArea(self):
        print("%4.1f" %(self.length * self.width))


rect = Rectangle()
rect.getRect()
rect.setRect()
rect.getRect()
rect.getArea()
