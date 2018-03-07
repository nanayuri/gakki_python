import requests
import bs4
import openpyxl
import re


def open_url(url):
    res = requests.get(url)
    return res


def find_data(res):
    data = []
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    content = soup.find(id="int-table__wrapper")
    target = iter(content.find_all("td", "column"))
    for each in target:
        print(each.text)
        data.append([
            each.text,
            re.search(r'\d*', next(target).text).group(),
            re.search(r'\w*\s*\w*\s*(\w*)', next(target).text).group(),
            re.search(r'\w*\s*\w*', next(target).text).group(),
            re.search(r'\d*', next(target).text).group(),
            re.search(r'\d*', next(target).text).group(),
            re.search(r'\d*', next(target).text).group(),
            re.search(r'\d*', next(target).text).group(),
            re.search(r'\d*', next(target).text).group()
                ])
    return data


def to_excel(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['2017 rank', '2016 rank', 'Institution name', 'Country', 'Academic reputation', 'Employer reputation', 'Citations', 'Research impact', 'Score'])
    for each in data:
        ws.append(each)
    wb.save("2017 QS Philosophy Rankings.xlsx")


def main():
    url = "http://dailynous.com/2017/03/08/2017-qs-philosophy-rankings-released/"
    res = open_url(url)
    data = find_data(res)
    to_excel(data)


if __name__ == "__main__":
    main()
