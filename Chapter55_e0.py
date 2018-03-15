import urllib.request

#url = 'http://whatismyip.org/homepage/'
url = 'http://www.whatismyip.com.tw/'

proxy_support = urllib.request.ProxyHandler({'HTTP': '119.6.144.73:81'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]
urllib.request.install_opener(opener)
# req = urllib.request.Request(url)

#req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
