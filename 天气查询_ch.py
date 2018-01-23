import urllib.request
import json
import pickle
# 建立城市字典
pickle_file = open('city_data.pk1', 'rb')
city = pickle.load(pickle_file)
print(city)
password = input('请输入城市:')
name1 = city[password]
File1 = urllib.request.urlopen('http://e.weather.com.cn/d/index/'+name1+'.shtml')#打开url
print('http://e.weather.com.cn/d/index/'+name1+'.shtml')
weatherHTML = File1.read() # 读入打开的url
# weatherJSON = json.JSONDecoder.decode(weatherHTML) # 创建json
weatherJSON = json.JSONDecoder.decode(weatherHTML, 3)
weatherInfo = weatherJSON['weatherinfo']
#打印信息
print('城市：', weatherInfo['city'])
print('时间：', weatherInfo['date_y'])
print('24小时天气：')
print('温度：', weatherInfo['temp1'])
print('天气：', weatherInfo['weather1'])
print('风速：', weatherInfo['wind1'])
print('紫外线：', weatherInfo['index_uv'])
print('穿衣指数：', weatherInfo['index_d'])
print('48小时天气：')
print('温度：', weatherInfo['temp2'])
print('天气：', weatherInfo['weather2'])
print('风速：', weatherInfo['wind2'])
print('紫外线：', weatherInfo['index48_uv'])
print('穿衣指数：', weatherInfo['index48_d'])
print('72小时天气：')
print('温度：', weatherInfo['temp3'])
print('天气：', weatherInfo['weather3'])
print('风速：', weatherInfo['wind3'])
input('按任意键退出：')