# 生成图片验证码
from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random
from pytesser3 import *

# 定义验证码的宽度和高度
width  = 110
height = 40
# 干扰点个数
disbPoint = 500
# 干扰线条数
disbLine  = 5

# 定义返回单个随机字符的方法
def rndChar():
    return chr(random.randint(65,90))

# 定义方法返回随机颜色
def rndColor():
    return random.randint(0,200)

# 定义方法返回随机字体大小
def rndFize():
    return random.randint(20,35)

# x轴上随机
def rndX():
    return random.randint(0, width)

# y轴上随机
def rndY():
    return random.randint(0, height)

def identify(im):
    imgry = im.convert('L')
    imgry.show()
    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    out = imgry.point(table, '1')
    out.show()
    image = Image.open(im)
    print(pytesser3.image_file_to_string(im))


# 创建画布和draw对象
im   = Image.new('RGB', (width,height), (227,227,227))
draw = ImageDraw.Draw(im)

# 循环 不同颜色
for x in range(4):
    # 加载字体,随机颜色
    fnt = ImageFont.truetype("C:\\Program Files\\Python36\\Lib\\site-packages\\matplotlib\\mpl-data\\fonts\\ttf\\DejaVuSerif.ttf", rndFize())
    draw.text((29*x,5),rndChar(),font=fnt,fill=(rndColor(),rndColor(),rndColor()))

# 循环 干扰点
for y in range(disbPoint):
    draw.point((rndX(),rndY()), fill=(rndColor(),rndColor(),rndColor()))

# 添加干扰线
for z in range(disbLine):
    draw.line([(rndX(),rndY()), (rndX(),rndY())], fill=(rndColor(),rndColor(),rndColor()), width=1)

im.filter(ImageFilter.EDGE_ENHANCE).show()
identify(im)

