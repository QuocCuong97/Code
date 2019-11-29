import requests
from bs4 import BeautifulSoup
from objects import ObjectCrawl
from json_execute import export_to_json


class FoxEbook(object):

    def __init__(self):
        self.url = "https://www.foxebook.net/category/computers-internet/"
        self.homepage = "https://www.foxebook.net"
        self.source = "FoxEbook"

    def get_dom(self, val):
        self.page_id = val
        page = requests.get(self.url + 'page/{}'.format(self.page_id))
        dom = BeautifulSoup(page.text, 'html5lib')
        return dom

    def get_objects(self):
        try:
            start_page = 1
            list_objects = []
            while start_page <= 2:
                html_dom = self.get_dom(start_page)
                mark = html_dom.findAll(class_="row book-top")
                for x in mark:
                    title_search = x.find(attrs={'class' : 'col-md-9'})
                    title_search = title_search.h3
                    self.title = title_search.string
                    
                    link_search = title_search.a
                    self.link = self.homepage + link_search['href']

                    images_search = x.find(attrs={'class' : 'col-md-3'})
                    images_search = images_search.img
                    self.images= images_search['src']

                    new_post = ObjectCrawl(self.title, self.link, self.images, self.source)
                    dic = new_post.to_dict()
                    list_objects.append(dic)
                start_page+=1
        except:
            pass
        return list_objects
