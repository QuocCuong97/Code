import sqlite3
from json_execute import load_from_json

def insert_data(para_1, para_2, para_3, para_4, para_5):
    my_connect = sqlite3.connect('/home/cuongnq/crawl/Pricelist/db.sqlite3')
    my_cursor = my_connect.cursor()
    my_cursor.execute("INSERT INTO {} ({}, {}) values ('{}', '{}')".format(para_1, para_2, para_3, para_4, para_5))
    my_connect.commit()
    
def update_data(para_1, para_2, para_3, para_4, para_5):
    my_connect = sqlite3.connect('/home/cuongnq/crawl/Pricelist/db.sqlite3')
    my_cursor = my_connect.cursor()
    my_cursor.execute("UPDATE {} SET {} = '{}' WHERE {} = `{}`".format(para_1, para_2, para_3, para_4, para_5))
    my_connect.commit()

val = load_from_json('/home/cuongnq/crawl/Pricelist/code/output.json')

for x in val:
    vendor = x["source"]
    homepage = x["homepage"]
    sale_price_vn = x[".vn"]
    sale_price_com = x[".com"]
    sale_price_comvn = x[".com.vn"]
    sale_price_net = x[".net"]
    sale_price_org = x[".org"]
    sale_price_info = x[".info"]
    insert_data('home_vendor', 'name', 'homepage', vendor, homepage)
    insert_data('home_vn', 'sale_price', 'origin_price', sale_price_vn, '0')
    insert_data('home_comvn', 'sale_price', 'origin_price', sale_price_comvn, '0')
    insert_data('home_com', 'sale_price', 'origin_price', sale_price_com, '0')
    insert_data('home_net', 'sale_price', 'origin_price', sale_price_net, '0')
    insert_data('home_org', 'sale_price', 'origin_price', sale_price_org, '0')
    insert_data('home_info', 'sale_price', 'origin_price', sale_price_info, '0')



