import json
import urllib.request
import mysql.connector as mariadb
from bs4 import BeautifulSoup

table_name = 'web_crawling'

def get_list():
    try:
        start = 1
        list_output = []
        while True:
            url =  'https://news.cloud365.vn/page/{}'.format(start) 
            page = urllib.request.urlopen(url)
            html_dom = BeautifulSoup(page, 'html5lib')
            mark = html_dom.findAll(class_="post-header")
            source_search = html_dom.find(['h2', {'class', 'blog-title'}])
            source_search = source_search.find('a')
            source = source_search['href']

            for x in mark:
                title_search = x.find(['a', "href"])
                title = title_search.string

                link_search = x.find(['a', "href"])
                link = link_search['href']

                time_search = x.find(attrs={'class' : 'post-date'})
                time = time_search.string

                author_search = x.find(attrs={'class' : 'post-author'})
                author = author_search.string

                dic = {key: value for key, value in [('Title', title), ('Link', link), ('Date Created', time), ('Author', author), ('Source', source)]}
                list_output.append(dic)
            start+=1        
    except:
        pass
    return list_output

def import_to_json(material, json_file):
    output = json.dumps(material, indent=4, ensure_ascii=False)
    op = open(json_file, 'w', encoding="utf-8")
    op.write(output)
    op.close()

lst = get_list()
import_to_json(lst, 'output.json')

lst.reverse()

mydb = mariadb.connect(host='localhost', user='mariadb-user', password='P@ssw0rd', database='new_database')
mycursor = mydb.cursor()
try:
    mycursor.execute('CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), link VARCHAR(191), date VARCHAR(40), author VARCHAR(40), source VARCHAR(40), UNIQUE(link))'.format(table_name))
except:
    pass

for x in lst:
    try:
        sql = "INSERT INTO {} (title, link, date, author, source) VALUES (%s, %s, %s, %s, %s)".format(table_name)
        val = (x['Title'], x['Link'], x['Date Created'], x['Author'], x['Source'])
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        pass
