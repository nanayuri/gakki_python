# coding=utf-8
import sys
import os
#os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
try:
    from pyocr import pyocr
    from PIL import Image
except ImportError:
    raise SystemExit
#导入库
tools = pyocr.get_available_tools()[:]
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
#查找OCR引擎
print("Using '%s'" % (tools[0].get_name()))
print(tools[0].image_to_string(Image.open('v.jpg'),lang='chi_sim'))
