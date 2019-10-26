from bs4 import BeautifulSoup
import urllib.request
import json

url =  'https://vnexpress.net/'
page = urllib.request.urlopen(url)
html_dom = BeautifulSoup(page, 'html5lib')

mark = html_dom.h1.a
title = mark.string
title = title.strip()
print(title)

link = mark['href']
print(link)

dic = {key: value for key, value in [('Title', title), ('Link', link)]}
output = json.dumps(dic, indent=4, ensure_ascii=False)
op = open('output.json', 'w', encoding="utf-8")
op.write(output)
