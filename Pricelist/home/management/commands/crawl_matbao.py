import requests
from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup

homepage = "https://www.matbao.net/"
urls = "https://www.matbao.net/ten-mien/bang-gia-ten-mien.html"
source = "MatBao"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("u", text=".vn")
    mark_origin_parent = mark_origin.parent.parent.parent
    origin_price = mark_origin_parent.contents[11].text.strip("\n đ")
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .vn'})
    mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
    sale_price = mark_sale_content[0].strip()
    return [origin_price, sale_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"href":"https://www.matbao.net/ten-mien/.com.html"})
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5].contents[3]
    origin_price = mark_origin_parent_content.text.strip().strip(' đ')
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .com'})
    mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
    sale_price = mark_sale_content[0].strip()
    return [origin_price, sale_price]

def get_com_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("u", text=".net.vn/ .biz.vn/ .com.vn")
    mark_origin_parent = mark_origin.parent.parent.parent
    origin_price = mark_origin_parent.contents[11].text.strip("\n đ")
    try:
        dom_sale = get_dom(homepage)
        mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .com.vn'})
        mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
        sale_price = mark_sale_content[0].strip()
    except:
        sale_price = origin_price
    return [origin_price, sale_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"href":"https://www.matbao.net/ten-mien/.net.html"})
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5].contents[3]
    origin_price = mark_origin_parent_content.text.strip().strip(' đ')
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .net'})
    mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
    sale_price = mark_sale_content[0].strip()
    return [origin_price, sale_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"href":"https://www.matbao.net/ten-mien/.org.html"})
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5].contents[1]
    origin_price = mark_origin_parent_content.text.strip().strip(' đ')
    try:
        dom_sale = get_dom(homepage)
        mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .org'})
        mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
        sale_price = mark_sale_content[0].strip()
    except:
        sale_price = origin_price
    return [origin_price, sale_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find(attrs={"href":"https://www.matbao.net/ten-mien/.info.html"})
    mark_origin_parent = mark_origin.parent.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5].contents[3]
    origin_price = mark_origin_parent_content.text.strip().strip(' đ')
    try:
        dom_sale = get_dom(homepage)
        mark_sale = dom_sale.find(attrs={'title' : 'Tên miền .info'})
        mark_sale_content = mark_sale.b.contents[0].strip().split('đ')
        sale_price = mark_sale_content[0].strip()
    except:
        sale_price = origin_price
    return [origin_price, sale_price]

class Command(BaseCommand):
    help = 'Crawl PriceList'

    def add_arguments(self, parser):
        parser.add_argument('-vn',action='store_true', help='crawl .vn')
        parser.add_argument('-comvn',action='store_true', help='crawl .com.vn')
        parser.add_argument('-com',action='store_true', help='crawl .com')
        parser.add_argument('-net',action='store_true', help='crawl .net')
        parser.add_argument('-org',action='store_true', help='crawl .org')
        parser.add_argument('-info',action='store_true', help='crawl .info')

    def handle(self, *args, **kwargs):
        if kwargs['vn']:
            print(get_vn())
        elif kwargs['comvn']:
            print(get_com_vn())
        elif kwargs['com']:
            print(get_com())
        elif kwargs['net']:
            print(get_net())
        elif kwargs['org']:
            print(get_org())
        elif kwargs['info']:
            print(get_info())
        else:
            print("Invalid options! Please type '-h' for help")
    

        