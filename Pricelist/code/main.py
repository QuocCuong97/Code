import json
import re
import requests
import urllib.request
from bs4 import BeautifulSoup
from json_execute import load_from_json, export_to_json, to_dict


list_price = []


class MatBao(object):

    def __init__(self):
        self.url = "https://www.matbao.net/"
        self.homepage = "https://www.matbao.net/"
        self.source = "MatBao"
        self.html_dom = self.get_dom()

    def get_dom(self):
        page = requests.get(self.url)
        dom = BeautifulSoup(page.text, 'html5lib')
        return dom
    
    def get_vn(self):
        mark = self.html_dom.find(attrs={'title' : 'Tên miền .vn'})
        mark_price = mark.b.contents[0].strip().split('đ')
        price = mark_price[0].strip()
        return price

    def get_com(self):
        mark = self.html_dom.find(attrs={'title' : 'Tên miền .com'})
        mark_price = mark.b.contents[0].strip().split('đ')
        price = mark_price[0].strip()
        return price

    def get_net(self):
        mark = self.html_dom.find(attrs={'title' : 'Tên miền .net'})
        mark_price = mark.b.contents[0].strip().split('đ')
        price = mark_price[0].strip()
        return price

    def get_com_vn(self):
        url = "https://www.matbao.net/ten-mien/bang-gia-ten-mien.html"
        page = requests.get(url)
        dom = BeautifulSoup(page.text, 'html5lib')
        mark = dom.find("u", text=".net.vn/ .biz.vn/ .com.vn")
        mark_parent = mark.parent.parent.parent
        price = mark_parent.contents[11].text.strip("\n đ")
        return price

    def get_org(self):
        url = "https://www.matbao.net/ten-mien/bang-gia-ten-mien.html"
        page = requests.get(url)
        dom = BeautifulSoup(page.text, 'html5lib')
        mark = dom.find("a", attrs={"title": "Tên miền .org"})
        mark_parent = mark.parent.parent.parent.parent
        price = mark_parent.contents[5].text.strip("\n đ")
        return price

    def get_info(self):
        url = "https://www.matbao.net/ten-mien/bang-gia-ten-mien.html"
        page = requests.get(url)
        dom = BeautifulSoup(page.text, 'html5lib')
        mark = dom.find("a", attrs={"title": "Tên miền .info"})
        mark_parent = mark.parent.parent.parent.parent
        mark_price = mark_parent.contents[5]
        price = mark_price.contents[3].text.strip("\n đ")
        return price

    def get_dict(self):
        dic = to_dict(self.source, self.homepage, self.get_vn(), self.get_com(), self.get_com_vn(), self.get_net(), self.get_org(), self.get_info())
        list_price.append(dic)


class NhanHoa(MatBao):

    def __init__(self):
        self.url = "https://nhanhoa.com/"
        self.homepage = "https://nhanhoa.com/"
        self.source = "NhanHoa" 
        self.html_dom = self.get_dom()
    
    def get_vn(self):
        mark = self.html_dom.find("figure", text=".vn")
        mark_sibling = mark.nextSibling.nextSibling
        price = mark_sibling.p.text.strip("đ")
        return price

    def get_com(self):
        mark = self.html_dom.find("figure", text=".com")
        mark_sibling = mark.nextSibling.nextSibling
        price = mark_sibling.p.string.strip("đ")
        return price

    def get_net(self):
        mark = self.html_dom.find("figure", text=".net")
        mark_sibling = mark.nextSibling.nextSibling
        price = mark_sibling.p.string.strip("đ")
        return price

    def get_com_vn(self):
        mark = self.html_dom.find("figure", text=".com.vn")
        mark_sibling = mark.nextSibling.nextSibling
        price = mark_sibling.p.string.strip("đ")
        return price

    def get_org(self):
        mark = self.html_dom.find("figure", text=".org")
        mark_sibling = mark.nextSibling.nextSibling
        price = mark_sibling.p.string.strip("đ")
        return price

    def get_info(self):
        mark = self.html_dom.find("figure", text=".info")
        mark_sibling = mark.nextSibling.nextSibling
        price = mark_sibling.p.string.strip("đ")
        return price

    def get_dict(self):
        dic = to_dict(self.source, self.homepage, self.get_vn(), self.get_com(), self.get_com_vn(), self.get_net(), self.get_org(), self.get_info())
        list_price.append(dic)


class PAVietNam(MatBao):

    def __init__(self):
        self.url = "https://www.pavietnam.vn/en/ten-mien-bang-gia.html"
        self.homepage = "https://www.pavietnam.vn/"
        self.source = "P.A VietNam"
        self.html_dom = self.get_dom()
        
    def get_vn(self):
        url = "https://www.pavietnam.vn/en/uu-dai-ten-mien-viet-nam.html"
        page = requests.get(url)
        dom = BeautifulSoup(page.text, "html5lib")
        mark = dom.find("strong", text=".VN")
        price = mark.nextSibling.nextSibling.string + ".000"
        return price

    def get_com_vn(self):
        url = "https://www.pavietnam.vn/en/uu-dai-ten-mien-viet-nam.html"
        page = requests.get(url)
        dom = BeautifulSoup(page.text, "html5lib")
        mark = dom.find("strong", text=".COM.VN")
        price = mark.nextSibling.nextSibling.string +".000"
        return price

    def get_com(self):
        mark = self.html_dom.find('span', attrs={"id": "com"})
        mark_parent = mark.parent.parent
        mark_content = mark_parent.contents[5]
        price = mark_content.contents[1].text.strip("d")
        return price

    def get_org(self):
        mark = self.html_dom.find('span', attrs={"id": "org"})
        mark_parent = mark.parent.parent
        mark_content = mark_parent.contents[5]
        price = mark_content.contents[1].text.strip("d")
        return price

    def get_net(self):
        mark = self.html_dom.find('span', attrs={"id": "net"})
        mark_parent = mark.parent.parent
        mark_content = mark_parent.contents[5]
        price = mark_content.contents[1].text.strip("d")
        return price

    def get_info(self):
        mark = self.html_dom.find('span', attrs={"id": "info"})
        mark_parent = mark.parent.parent
        mark_content = mark_parent.contents[5]
        price = mark_content.contents[1].text.strip("d")
        return price

    def get_dict(self):
        dic = to_dict(self.source, self.homepage, self.get_vn(), self.get_com(), self.get_com_vn(), self.get_net(), self.get_org(), self.get_info())
        list_price.append(dic)


class ESC(MatBao):

    def __init__(self):
        self.url = "https://esc.vn/"
        self.homepage = "https://esc.vn/"
        self.source = "ESC"
        self.html_dom = self.get_dom()

    def get_vn(self):
        mark = self.html_dom.find(attrs={"alt": "tên miền .vn"})
        mark_parent = mark.parent
        mark_parent_sibling = mark_parent.nextSibling
        price = mark_parent_sibling.string.strip("K") + ".000"
        return price

    def get_com_vn(self):
        mark = self.html_dom.find("span", text=".COM.VN")
        mark_sibling = mark.nextSibling
        price = mark_sibling.string.strip(" K") + ".000"
        return price

    def get_com(self):
        mark = self.html_dom.find(attrs={"src": "https://member.esc.vn/themes/default/img/domain_logo/.com.png"})
        mark_parent = mark.parent
        mark_parent_sibling = mark_parent.nextSibling
        price = mark_parent_sibling.string.strip(" K") + ".000"
        return price

    def get_net(self):
        url = "https://esc.vn/bang-gia-ten-mien/"
        page = requests.get(url)
        dom = BeautifulSoup(page.text, 'html5lib')
        mark = dom.find("p", text=".net")
        mark_parent = mark.parent
        mark_parent_sibling = mark_parent.nextSibling.nextSibling
        price = mark_parent_sibling.p.span.string
        return price

    def get_org(self):
        url = "https://esc.vn/bang-gia-ten-mien/"
        page = requests.get(url)
        dom = BeautifulSoup(page.text, 'html5lib')
        mark = dom.find("p", text=".org ")
        mark_parent = mark.parent
        mark_parent_sibling = mark_parent.nextSibling.nextSibling
        price = mark_parent_sibling.p.span.string
        return price

    def get_info(self):
        url = "https://esc.vn/bang-gia-ten-mien/"
        page = requests.get(url)
        dom = BeautifulSoup(page.text, 'html5lib')
        mark = dom.find("p", text=".info ")
        mark_parent = mark.parent
        mark_parent_sibling = mark_parent.nextSibling.nextSibling
        price = mark_parent_sibling.p.span.strong.string.strip()
        return price

    def get_dict(self):
        dic = to_dict(self.source, self.homepage, self.get_vn(), self.get_com(), self.get_com_vn(), self.get_net(), self.get_org(), self.get_info())
        list_price.append(dic)


class HostingViet(MatBao):

    def __init__(self):
        self.url = "https://hostingviet.vn/ten-mien/"
        self.homepage = "https://hostingviet.vn/"
        self.source = "HostingViet"
        self.html_dom = self.get_dom()

    def get_vn(self):
        mark = self.html_dom.find(class_="domain-table-common ten-mien-pho-bien-content")
        mark_content = mark.contents[1].contents[3].contents[3]
        price = mark_content.string.strip(" VNĐ")
        return price
    
    def get_com(self):
        mark = self.html_dom.find(class_="domain-table-common ten-mien-pho-bien-content")
        mark_content = mark.contents[1].contents[3].div
        price = mark_content.text.strip(" VNĐ")
        return price

    def get_com_vn(self):
        mark = self.html_dom.find(class_="domain-table-common ten-mien-pho-bien-content")
        mark_content = mark.contents[3].contents[3].div
        price = mark_content.string.strip(" VNĐ")
        return price

    def get_info(self):
        mark = self.html_dom.find(class_="domain-table-common ten-mien-pho-bien-content")
        mark_content = mark.contents[9].contents[3].div
        price = mark_content.string.strip().strip(" VNĐ")
        return price

    def get_org(self):
        mark = self.html_dom.find(class_="domain-table-common ten-mien-pho-bien-content")
        mark_content = mark.contents[11].contents[3].div
        price = mark_content.string.strip(" VNĐ")
        return price

    def get_net(self):
        mark = self.html_dom.find(class_="domain-table-common ten-mien-pho-bien-content")
        mark_content = mark.contents[13].contents[3].div
        price = mark_content.string.strip(" VNĐ")
        return price

    def get_dict(self):
        dic = to_dict(self.source, self.homepage, self.get_vn(), self.get_com(), self.get_com_vn(), self.get_net(), self.get_org(), self.get_info())
        list_price.append(dic)


class TenTen(MatBao):

    def __init__(self):
        self.url = "https://tenten.vn/bang-gia-ten-mien/"
        self.homepage = "https://tenten.vn/"
        self.source = "TenTen"
        self.html_dom = self.get_dom()

    def get_vn(self):
        mark = self.html_dom.find("td", text=".vn")
        mark_parent = mark.parent
        price = mark_parent.contents[11].text.strip("\n đ")
        return price

    def get_com_vn(self):
        mark = self.html_dom.find("td", text=".com.vn | .net.vn | .biz.vn")
        mark_parent = mark.parent
        price = mark_parent.contents[11].text.strip("\n đ")
        return price

    def get_com(self):
        mark = self.html_dom.find(class_="k_bgtm k_tmqt")
        mark_sibling = mark.table.tbody
        mark_content = mark_sibling.contents[1]
        mark_price = mark_content.contents[4]
        price = mark_price.contents[1].text.strip("\n đ")
        return price

    def get_net(self):
        mark = self.html_dom.find(class_="k_bgtm k_tmqt")
        mark_sibling = mark.table.tbody
        mark_content = mark_sibling.contents[5]
        mark_price = mark_content.contents[4]
        price = mark_price.contents[1].text.strip("\n đ")
        return price

    def get_info(self):
        mark = self.html_dom.find(class_="k_bgtm k_tmqt")
        mark_sibling = mark.table.tbody
        mark_content = mark_sibling.contents[7]
        mark_price = mark_content.contents[4]
        price = mark_price.contents[1].text.strip("\n đ")
        return price

    def get_org(self):
        mark = self.html_dom.find(class_="k_bgtm k_tmqt")
        mark_sibling = mark.table.tbody
        mark_content = mark_sibling.contents[43]
        mark_price = mark_content.contents[4]
        price = mark_price.text.strip("\n đ")
        return price

    def get_dict(self):
        dic = to_dict(self.source, self.homepage, self.get_vn(), self.get_com(), self.get_com_vn(), self.get_net(), self.get_org(), self.get_info())
        list_price.append(dic)


class VHost(MatBao):

    def __init__(self):
        self.url = "https://vhost.vn/ten-mien/"
        self.homepage = "https://vhost.vn/"
        self.source = "VHost"
        self.html_dom = self.get_dom()

    def get_vn(self):
        mark = self.html_dom.find(attrs={"id": "ptiv8s0NDNac"})
        mark_content = mark.tbody.contents[7]
        mark_price = mark_content.contents[2]
        price = mark_price.text.strip(" VND").replace(",", ".")
        return price

    def get_com_vn(self):
        mark = self.html_dom.find(attrs={"id": "ptiv8s0NDNac"})
        mark_content = mark.tbody.contents[8]
        mark_price = mark_content.contents[2]
        price = mark_price.text.strip(" VND").replace(",", ".")
        return price

    def get_com(self):
        mark = self.html_dom.find(attrs={"id": "ptiv8s0NDNac"})
        mark_content = mark.tbody.contents[1]
        mark_price = mark_content.contents[2]
        price = mark_price.text.strip(" VND").replace(",", ".")
        return price

    def get_net(self):
        mark = self.html_dom.find(attrs={"id": "ptiv8s0NDNac"})
        mark_content = mark.tbody.contents[2]
        mark_price = mark_content.contents[2]
        price = mark_price.text.strip(" VND").replace(",", ".")
        return price

    def get_org(self):
        mark = self.html_dom.find(attrs={"id": "ptiv8s0NDNac"})
        mark_content = mark.tbody.contents[3]
        mark_price = mark_content.contents[2]
        price = mark_price.text.strip(" VND").replace(",", ".")
        return price

    def get_info(self):
        mark = self.html_dom.find(attrs={"id": "ptiv8s0NDNac"})
        mark_content = mark.tbody.contents[5]
        mark_price = mark_content.contents[2]
        price = mark_price.text.strip(" VND").replace(",", ".")
        return price

    def get_dict(self):
        dic = to_dict(self.source, self.homepage, self.get_vn(), self.get_com(), self.get_com_vn(), self.get_net(), self.get_org(), self.get_info())
        list_price.append(dic)


class HostVN(MatBao):

    def __init__(self):
        self.url = "https://hostvn.net/ten-mien"
        self.homepage = "https://hostvn.net/"
        self.source = "HostVN"
        self.html_dom = self.get_dom()

    def get_vn(self):
        mark = self.html_dom.find("span", text=".vn")
        mark_parent = mark.parent.parent
        price = mark_parent.contents[2].strip("\n đ")
        return price

    def get_com(self):
        mark = self.html_dom.find("span", text=".com")
        mark_parent = mark.parent.parent
        price = mark_parent.contents[2].strip("\n đ")
        return price

    def get_net(self):
        return "Not Crawl Yet"
        # mark = self.html_dom.find("strong", text="net")
        # mark_parent = mark.parent
        # # price = mark_parent.contents[2].strip()
        # return mark_parent

    def get_org(self):
        mark = self.html_dom.find("span", text=".org")
        mark_parent = mark.parent.parent
        price = mark_parent.contents[2].strip("\n đ")
        return price

    def get_info(self):
        mark = self.html_dom.find("span", text=".info")
        mark_parent = mark.parent.parent
        price = mark_parent.contents[2].strip("\n đ")
        return price

    def get_com_vn(self):
        return "Not Crawl Yet"
    #     mark = self.html_dom.find("span", text=".com.vn")
    #     mark_parent = mark.parent.parent
    #     price = mark_parent.contents[2].strip()
    #     return price

    def get_dict(self):
        dic = to_dict(self.source, self.homepage, self.get_vn(), self.get_com(), self.get_com_vn(), self.get_net(), self.get_org(), self.get_info())
        list_price.append(dic)


class BKNS(MatBao):

    def __init__(self):
        self.url = "https://www.bkns.vn/"
        self.homepage = "https://www.bkns.vn/"
        self.source = "BKNS"
        self.html_dom = self.get_dom()

    def get_vn(self):
        mark = self.html_dom.find("p", text=".vn")
        mark_sibling = mark.nextSibling
        price = mark_sibling.text.strip('đ/năm')
        return price

    def get_com(self):
        mark = self.html_dom.find("p", text=".com")
        mark_sibling = mark.nextSibling
        price = mark_sibling.text.strip('đ/năm')
        return price

    def get_com_vn(self):
        mark = self.html_dom.find("p", text=".com.vn")
        mark_sibling = mark.nextSibling
        price = mark_sibling.text.strip('đ/năm')
        return price

    def get_net(self):
        url = "https://www.bkns.vn/ten-mien/bang-gia-ten-mien.html"
        page = requests.get(url)
        dom = BeautifulSoup(page.text, 'html5lib')
        mark = dom.find("td", text=".net")
        mark_parent = mark.parent
        price = mark_parent.contents[2].text.strip('đ/năm')
        return price

    def get_org(self):
        url = "https://www.bkns.vn/ten-mien/bang-gia-ten-mien.html"
        page = requests.get(url)
        dom = BeautifulSoup(page.text, 'html5lib')
        mark = dom.find("td", text=".org")
        mark_parent = mark.parent
        price = mark_parent.contents[2].text.strip('đ/năm')
        return price

    def get_info(self):
        mark = self.html_dom.find("p", text=".info")
        mark_sibling = mark.nextSibling
        price = mark_sibling.text.strip('đ/năm')
        return price

    def get_dict(self):
        dic = to_dict(self.source, self.homepage, self.get_vn(), self.get_com(), self.get_com_vn(), self.get_net(), self.get_org(), self.get_info())
        list_price.append(dic)


class VinaHost(object):

    def __init__(self):
        self.url = "https://vinahost.vn/bang-gia-ten-mien.html"
        self.homepage = "https://vinahost.vn/"
        self.source = "VinaHost"
        self.html_dom = self.get_dom()
        
    def get_dom(self):
        header = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
        page = requests.get(self.url, headers=header)
        dom = BeautifulSoup(page.text, "html5lib")
        return dom

    def get_vn(self):
        mark = self.html_dom.find('td', text=".vn")
        mark_parent = mark.parent
        mark_content = mark_parent.contents[11]
        price = mark_content.string.strip(" VNĐ").replace(",", ".")
        return price
    
    def get_com_vn(self):
        mark = self.html_dom.find('td', text=".com.vn | .net.vn | .biz.vn")
        mark_parent = mark.parent
        mark_content = mark_parent.contents[11]
        price = mark_content.string.strip("/năm").strip(" VNĐ").replace(",", ".")
        return price

    def get_com(self):
        mark = self.html_dom.find('td', text=".com | .com.co | .cc | .xyz")
        mark_parent = mark.parent
        mark_content = mark_parent.contents[3]
        price = mark_content.string.strip("/năm").strip(" VNĐ").replace(",", ".")
        return price
    
    def get_net(self):
        mark = self.html_dom.find('td', text=".net")
        mark_parent = mark.parent
        mark_content = mark_parent.contents[3]
        price = mark_content.string.strip("/năm").strip(" VNĐ").replace(",", ".")
        return price

    def get_org(self):
        mark = self.html_dom.find('td', text=".org")
        mark_parent = mark.parent
        mark_content = mark_parent.contents[3]
        price = mark_content.string.strip("/năm").strip(" VNĐ").replace(",", ".")
        return price

    def get_info(self):
        mark = self.html_dom.find('td', text=".info")
        mark_parent = mark.parent
        mark_content = mark_parent.contents[3]
        price = mark_content.string.strip("/năm").strip(" VNĐ").replace(",", ".")
        return price

    def get_dict(self):
        dic = to_dict(self.source, self.homepage, self.get_vn(), self.get_com(), self.get_com_vn(), self.get_net(), self.get_org(), self.get_info())
        list_price.append(dic)


def crawl(*args):
    for x in args:
        x.get_dict()
    export_to_json(list_price, "/home/cuongnq/crawl/Pricelist/code/output.json")

def main():
    web_1 = NhanHoa()
    web_2 = MatBao()
    web_3 = PAVietNam()
    web_4 = HostingViet()
    web_5 = ESC()
    web_6 = VinaHost()
    web_7 = HostVN()
    web_8 = VHost()
    web_9 = TenTen()
    web_10 = BKNS()
    crawl(web_1, web_2, web_3, web_4, web_5, web_6, web_7, web_8, web_9, web_10)


main()



# class INet(MatBao):
#     def __init__(self):
#         self.url = "https://inet.vn/"
#         self.source = "iNET"
#     def get_vn(self):
#         html_dom = self.get_dom()
#         mark = html_dom.find(attrs={"alt": ".vn"})
#         print(mark)
        # mark = html_dom.find('body')
        # mark = mark.string
        # val = load_from_json(mark)
        # print(val[0][0])


# class TND(MatBao):
#     def __init__(self):
#         self.url = ("https://cloud.tnd.vn/cart.php?a=add&domain=register")
#         self.source = ("TND")
#     def get_vn(self):
#         html_dom = self.get_dom()
#         mark = html_dom.find("td", text=".vn")
#         print(html_dom)