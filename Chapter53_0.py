import urllib

response = urllib.request.urlopen("http://www.fishc.com")
html = response.read()
html = html.decode("utf-8")
print(html[:300])