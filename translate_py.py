import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

content = input('请输入需要翻译的内容:')
url = 'https://zhongwenzhuanpinyin.51240.com/web_system/51240_com_www/system/file/zhongwenzhuanpinyin/data/?ajaxtimestamp=1520933757427'
data = {}
data['zwzyp_zhongwen'] = content
data['zwzyp_shengdiao'] = '0'
data['zwzyp_wenzi'] = '0'
data['zwzyp_jiange'] = '1'
data['zwzyp_duozhongduyin'] = '0'


data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')
print(html)
soup = BeautifulSoup(html)
print(soup.textarea.string)


#print("翻译结果:%s" % target['translateResult'][0][0]['tgt'])