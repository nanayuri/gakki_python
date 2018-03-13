import urllib
import chardet


url = input("请输入URL:")
response = urllib.request.urlopen(url).read()
dc = chardet.detect(response)['encoding']
print("该网页使用的编码是:%s" % dc)
