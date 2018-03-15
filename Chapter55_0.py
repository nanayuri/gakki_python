import urllib.request
from bs4 import BeautifulSoup

url = 'http://baike.baidu.com/view/284853.htm'
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)