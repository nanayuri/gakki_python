import urllib.request
import chardet


def open_url(url):
    response = urllib.request.urlopen(url).read()
    dc = chardet.detect(response)['encoding']
    html = response.decode(dc)
    return html, dc


i = 0


with open("urls.txt") as f:
    for each_line in f.readlines():
        ct = open_url(each_line)
        content = ct[0]
        dcod = ct[1]
        i += 1
        with open("url_" + str(i) + '.txt', 'w', encoding=dcod) as fs:
            fs.write(content)
