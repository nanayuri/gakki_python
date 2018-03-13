# -- coding:gbk --
import re
# import urllib, urllib2, cookielib
import http.cookiejar
import urllib.request
import urllib.parse
import urllib

loginurl = 'https://www.douban.com/accounts/login'
cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

params = {
    "form_email": "email ",
    "form_password": "pwd",
    "source": "index_nav"  # 没有的话登录不成功
}
data = urllib.parse.urlencode(params).encode('utf-8')
# 从首页提交登录
response = urllib.request.urlopen(loginurl, data)

# 验证成功跳转至登录页
if response.geturl() == "https://www.douban.com/accounts/login":
    html = response.read().decode('utf-8')

    # 验证码图片地址
    imgurl = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url = imgurl.group(1)
        # 将图片保存至同目录下
        res = urllib.request.urlretrieve(url, 'v.jpg')
        # 获取captcha-id参数
        captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>', html)
        if captcha:
            vcode = input('请输入图片上的验证码：')
            params["captcha-solution"] = vcode
            params["captcha-id"] = captcha.group(1)
            params["user_login"] = "登录"
            # 提交验证码验证
            response = opener.open(loginurl, urllib.parse.urlencode(params))
            ''' 登录成功跳转至首页 '''
            if response.geturl() == "http://www.douban.com/":
                print('login success ! ')
