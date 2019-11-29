import mysql.connector as mariadb

class Mariadb(object):

    def __init__(self, para_host, para_username, para_passwd, para_db):
        self.host = para_host
        self.username = para_username
        self.passwd = para_passwd
        self.database = para_db

    def connect(self):
        myconnect = mariadb.connect(host = self.host, user = self.username, password = self.passwd, database = self.database)
        return myconnect

    def close(self, myconnect):
        myconnect.close()

    def query(self, myconnect, para_table):
        mycursor = myconnect.cursor()
        sql = 'SELECT telegram FROM {} ORDER BY ID DESC LIMIT 1'.format(para_table)
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        if myresult[0].strip() == 'True':
            return '1'
        else:
            return '0'

    def newest_link(self, myconnect, para_table):
        mycursor = myconnect.cursor()
        sql = 'SELECT link FROM {} ORDER BY ID DESC LIMIT 1'.format(para_table)
        mycursor.execute(sql)
        link = mycursor.fetchone()
        return link[0].strip()

    def newest_title(self, myconnect, para_table):
        mycursor = myconnect.cursor()
        sql = 'SELECT title FROM {} ORDER BY ID DESC LIMIT 1'.format(para_table)
        mycursor.execute(sql)
        title = mycursor.fetchone()
        return title[0].strip()

    def newest_images(self, myconnect, para_table):
        mycursor = myconnect.cursor()
        sql = 'SELECT images FROM {} ORDER BY ID DESC LIMIT 1'.format(para_table)
        mycursor.execute(sql)
        title = mycursor.fetchone()
        return title[0].strip()

    def update_true(self, myconnect, para_table):
        mycursor = myconnect.cursor()
        sql = 'UPDATE {} SET telegram = "True" ORDER BY id DESC LIMIT 1'.format(para_table)
        mycursor.execute(sql)
        myconnect.commit()

    def insert(self, para_list, myconnect, para_table):
        for x in para_list:
            try:
                sql = 'INSERT INTO {} (title, link, images, source, telegram) VALUES (%s, %s, %s, %s, %s)'.format(para_table)
                val = (x['title'], x['link'], x['images'], x['source'], 'False')
                mycursor = myconnect.cursor()
                mycursor.execute(sql, val)
                myconnect.commit()
            except:
                pass

    def create_table(self, myconnect, para_table):
        mycursor = myconnect.cursor()
        try:
            mycursor.execute('CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), link VARCHAR(191), images VARCHAR(191), source VARCHAR(40), telegram VARCHAR(10), UNIQUE(link))'.format(para_table))
        except:
            pass