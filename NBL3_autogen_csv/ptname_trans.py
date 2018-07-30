import http.client
import hashlib
import json
import urllib
import random


def baidu_translate(content):
    appid = '20180703000182287'
    secretKey = 'Z_vJ9kE9OUmgjFZati7f'
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = content
    print(q)
    fromLang = 'zh'  # 源语言
    toLang = 'en'  # 翻译后的语言
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
    dst = ''
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)
    # response是HTTPResponse对象
    response = httpClient.getresponse()
    jsonResponse = response.read().decode('utf-8')  # 获得返回的结果，结果为json格式
    print(jsonResponse)
    js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
    dst = str(js['trans_result'][0]['dst'])  # 取得翻译后的文本结果
    print(dst)  # 打印结果
    return dst


if __name__ == '__main__':
    list1 = []
    dict1 = {}
    with open('unkonw_label.txt', 'r') as f1:
        list1 = f1.readlines()
    for each in list1:
        each = each.replace('\n', '')
        dict1[each] = baidu_translate(each)
    with open('trans_res.csv', 'w') as f2:
        for each_line in dict1.items():
            f2.write(each_line[0] + ',' + each_line[1] + '\n')
