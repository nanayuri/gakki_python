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
    "source": "index_nav"  # û�еĻ���¼���ɹ�
}
data = urllib.parse.urlencode(params).encode('utf-8')
# ����ҳ�ύ��¼
response = urllib.request.urlopen(loginurl, data)

# ��֤�ɹ���ת����¼ҳ
if response.geturl() == "https://www.douban.com/accounts/login":
    html = response.read().decode('utf-8')

    # ��֤��ͼƬ��ַ
    imgurl = re.search('<img id="captcha_image" src="(.+?)" alt="captcha" class="captcha_image"/>', html)
    if imgurl:
        url = imgurl.group(1)
        # ��ͼƬ������ͬĿ¼��
        res = urllib.request.urlretrieve(url, 'v.jpg')
        # ��ȡcaptcha-id����
        captcha = re.search('<input type="hidden" name="captcha-id" value="(.+?)"/>', html)
        if captcha:
            vcode = input('������ͼƬ�ϵ���֤�룺')
            params["captcha-solution"] = vcode
            params["captcha-id"] = captcha.group(1)
            params["user_login"] = "��¼"
            # �ύ��֤����֤
            response = opener.open(loginurl, urllib.parse.urlencode(params))
            ''' ��¼�ɹ���ת����ҳ '''
            if response.geturl() == "http://www.douban.com/":
                print('login success ! ')
