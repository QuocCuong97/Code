import requests
import os
from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup

homepage = "https://nhanhoa.com/"
urls = "https://nhanhoa.com/trang/ten-mien/bang-gia-ten-mien.html"
source = "NhanHoa"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".vn")
    mark_origin_parent = mark_origin.parent
    origin_price = mark_origin_parent.contents[11].text.strip(" đ")
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find("figure", text=".vn")
    mark_sale_sibling = mark_sale.nextSibling.nextSibling
    sale_price = mark_sale_sibling.p.text
    return [origin_price,sale_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".com")
    mark_origin_parent = mark_origin.parent
    origin_price = mark_origin_parent.contents[2].contents[0].text.strip(' đ')
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find("figure", text=".com")
    mark_sale_sibling = mark_sale.nextSibling.nextSibling
    sale_price = mark_sale_sibling.p.text
    return [origin_price, sale_price]

def get_com_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".net.vn/ .com.vn/ .biz.vn ")
    mark_origin_parent = mark_origin.parent
    origin_price = mark_origin_parent.contents[11].text.strip(" đ")
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find("figure", text=".com.vn")
    mark_sale_sibling = mark_sale.nextSibling.nextSibling
    sale_price = mark_sale_sibling.p.text
    return [origin_price, sale_price]

def get_net():
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find("figure", text=".net")
    mark_sale_sibling = mark_sale.nextSibling.nextSibling
    sale_price = mark_sale_sibling.p.text
    try:
        dom_origin = get_dom(urls)
        mark_origin = dom_origin.find("td", text=".net")
        mark_origin_parent = mark_origin.parent
        origin_price = mark_origin_parent.contents[11].text.strip(" đ")
    except:
        origin_price = sale_price
    return [origin_price, sale_price]

def get_org():
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find("figure", text=".org")
    mark_sale_sibling = mark_sale.nextSibling.nextSibling
    sale_price = mark_sale_sibling.p.text
    try:
        dom_origin = get_dom(urls)
        mark_origin = dom_origin.find("td", text=".org")
        mark_origin_parent = mark_origin.parent
        origin_price = mark_origin_parent.contents[11].text.strip(" đ")
    except:
        origin_price = sale_price
    return [origin_price, sale_price]

def get_info():
    dom_sale = get_dom(homepage)
    mark_sale = dom_sale.find("figure", text=".info")
    mark_sale_sibling = mark_sale.nextSibling.nextSibling
    sale_price = mark_sale_sibling.p.text
    try:
        dom_origin = get_dom(urls)
        mark_origin = dom_origin.find("td", text=".info")
        mark_origin_parent = mark_origin.parent
        origin_price = mark_origin_parent.contents[11].text.strip(" đ")
    except:
        origin_price = sale_price
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

