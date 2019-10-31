import json
import urllib.request
from bs4 import BeautifulSoup

def get_list():
    try:
        start = 1
        list_output = []
        while True:
            url =  'https://tecadmin.net/page/{}'.format(start) 
            page = urllib.request.urlopen(url)
            html_dom = BeautifulSoup(page, 'html5lib')

            mark = html_dom.findAll('h2', { "class" : "title home-post-title entry-title"})
            for x in mark:
                title_search = x.find('a')
                title = title_search.string

                link_search = x.contents[1]
                link = link_search['href']

                # time_search = html_dom.find(class_ = "post-date", attrs={"href", "{}".format(link)})
                # time = time_search.string

                dic = {key: value for key, value in [('Title', title), ('Link', link)]}
                list_output.append(dic)
            start+=1
    except: 
        pass
    return list_output