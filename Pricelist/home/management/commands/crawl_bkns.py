import os

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from home.models import Domain, Vendor

homepage = "https://www.bkns.vn/"
urls = "https://www.bkns.vn/ten-mien/bang-gia-ten-mien.html"
source = "BKNS"

def get_dom(url):
    page = requests.get(url)
    dom = BeautifulSoup(page.text, 'html5lib')
    return dom

def get_vn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("u", text=".vn")
    mark_origin_parent = mark_origin.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5]
    origin_price = mark_origin_parent_content.contents[2].string.strip(' đ')
    dom_sale = get_dom(homepage)
    mark = dom_sale.find("p", text=".vn")
    mark_sibling = mark.nextSibling
    sale_price = mark_sibling.text.strip('đ/năm')
    return [origin_price, sale_price]

def get_comvn():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("u", text=".net.vn/ .biz.vn/ .com.vn")
    mark_origin_parent = mark_origin.parent.parent.parent
    mark_origin_parent_content = mark_origin_parent.contents[5]
    origin_price = mark_origin_parent_content.contents[2].string.strip(' đ')
    dom_sale = get_dom(homepage)
    mark = dom_sale.find("p", text=".com.vn")
    mark_sibling = mark.nextSibling
    sale_price = mark_sibling.text.strip('đ/năm')
    return [origin_price, sale_price]

def get_com():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".com")
    mark_origin_sibling = mark_origin.nextSibling.nextSibling
    origin_price = mark_origin_sibling.contents[2].text
    dom_sale = get_dom(homepage)
    mark = dom_sale.find("p", text=".com")
    mark_sibling = mark.nextSibling
    sale_price = mark_sibling.text.strip('đ/năm')
    return [origin_price, sale_price]

def get_net():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".net")
    mark_origin_sibling = mark_origin.nextSibling.nextSibling
    origin_price = mark_origin_sibling.string
    try:
        dom_sale = get_dom(homepage)
        mark = dom_sale.find("p", text=".net")
        mark_sibling = mark.nextSibling
        sale_price = mark_sibling.text.strip('đ/năm')
    except:
        sale_price = origin_price
    return [origin_price, sale_price]

def get_org():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".org")
    mark_origin_sibling = mark_origin.nextSibling.nextSibling
    origin_price = mark_origin_sibling.string
    try:
        dom_sale = get_dom(homepage)
        mark = dom_sale.find("p", text=".org")
        mark_sibling = mark.nextSibling
        sale_price = mark_sibling.text.strip('đ/năm')
    except:
        sale_price = origin_price
    return [origin_price, sale_price]

def get_info():
    dom_origin = get_dom(urls)
    mark_origin = dom_origin.find("td", text=".info")
    mark_origin_sibling = mark_origin.nextSibling.nextSibling
    origin_price = mark_origin_sibling.contents[2].text
    try:
        dom_sale = get_dom(homepage)
        mark = dom_sale.find("p", text=".info")
        mark_sibling = mark.nextSibling
        sale_price = mark_sibling.text.strip('đ/năm')
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
        parser.add_argument('-a',action='store_true', help='crawl all')

    def handle(self, *args, **kwargs):
        if kwargs['vn']:
            lst_vn = get_vn()
            print(lst_vn)
            vendor_test = Vendor.objects.all().first()
            vn = Domain.objects.create(vendor=vendor_test, domain_type='vn', origin_price=lst_vn[0], sale_price=lst_vn[1])
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
