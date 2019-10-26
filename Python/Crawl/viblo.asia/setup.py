from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json

reg_url =  'https://viblo.asia'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()  
html_dom = BeautifulSoup(html, 'html5lib')

mark = html_dom.h3.a
title = mark.string
title = title.strip()
print(title)

link = mark['href']
link = str(reg_url) + link
print(link)

dic = {key: value for key, value in [('Title', title), ('Link', link)]}
output = json.dumps(dic, indent=4, ensure_ascii=False)
op = open('output.json', 'w', encoding="utf-8")
op.write(output)
