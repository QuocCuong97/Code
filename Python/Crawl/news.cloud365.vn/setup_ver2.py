import json
import urllib.request
from bs4 import BeautifulSoup

start = 1
list_output = []

try:
    while True:
        url =  'https://news.cloud365.vn/page/{}'.format(start) 
        page = urllib.request.urlopen(url)
        html_dom = BeautifulSoup(page, 'html5lib')

        mark = html_dom.findAll(class_="post-title")
        for x in mark:
            title_search = x.string
            title = title_search.strip()
            print(title)

            link_search = x.contents[0]
            link = link_search['href']
            print(link)

            time_search = html_dom.find(class_ = "post-date", attrs={"href", "{}".format(link)})
            time = time_search.string

            dic = {key: value for key, value in [('Title', title), ('Link', link), ('Date Created', time)]}
            list_output.append(dic)
        start+=1
except:
    pass

output = json.dumps(list_output, indent=4, ensure_ascii=False)
op = open('output.json', 'w', encoding="utf-8")
op.write(output)
op.close()