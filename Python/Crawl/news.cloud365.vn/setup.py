from bs4 import BeautifulSoup
import urllib.request
import json

url =  'https://news.cloud365.vn/'
page = urllib.request.urlopen(url)
html_dom = BeautifulSoup(page, 'html5lib')

mark = html_dom.find(class_="post-title")
title = mark.string
title = title.strip()
print(title)

mark_0 = mark.contents[0]
link = mark_0['href']
print(link)

dic = {key: value for key, value in [('Title', title), ('Link', link)]}
output = json.dumps(dic, indent=4, ensure_ascii=False)
op = open('output.json', 'w', encoding="utf-8")
op.write(output)

