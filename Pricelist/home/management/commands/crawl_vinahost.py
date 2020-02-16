import requests
import os
from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup

homepage = "https://vinahost.vn/"
urls = "https://vinahost.vn/bang-gia-ten-mien.html"
source = "VinaHost"

def get_dom(url):
    header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
    page = requests.get(url, headers=header)
    dom = BeautifulSoup(page.text, "html5lib")
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".vn")
    mark_origin_content = mark_origin.parent.contents[11]
    origin_price = mark_origin_content.string.strip(" VNĐ").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]

def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".com.vn | .net.vn | .biz.vn")
    mark_origin_content = mark_origin.parent.contents[11]
    origin_price = mark_origin_content.string.strip(" VNĐ").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".com | .com.co | .cc | .xyz")
    mark_origin_content = mark_origin.parent.contents[3]
    origin_price = mark_origin_content.string.strip("/năm").strip(" VNĐ").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".net")
    mark_origin_content = mark_origin.parent.contents[3]
    origin_price = mark_origin_content.string.strip("/năm").strip(" VNĐ").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".org")
    mark_origin_content = mark_origin.parent.contents[3]
    origin_price = mark_origin_content.string.strip("/năm").strip(" VNĐ").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find('td', text=".info")
    mark_origin_content = mark_origin.parent.contents[3]
    origin_price = mark_origin_content.string.strip("/năm").strip(" VNĐ").replace(",", ".")
    sale_price = origin_price
    return [origin_price,sale_price]


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
            print(get_comvn())
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
    

        