import os
import re
import subprocess
import json

# Function read database info
def read_info():
    x = open("settings.json", "r")
    y = x.read()
    global dic
    dic = json.loads(y)

# Function creat new Database
def creat_database():
    os.system("pip3 install mysql-connector-python")
    import mysql.connector as mariadb
    mydb = mariadb.connect(host=str(dic["host_access"]), user=str(dic["user_access"]), password=str(dic["password_access"]))
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE %s" %(str(dic["database_name"])))
    mycursor.execute("CREATE USER %s@%s IDENTIFIED BY '%s';" %(str(dic["mariauser"]), str(dic["host_access"]), str(dic["mariapass"])))
    mycursor.execute("GRANT ALL PRIVILEGES ON %s.* TO '%s'@'%s';" %(str(dic["database_name"]), str(dic["mariauser"]), str(dic["host_access"])))
    mycursor.execute("FLUSH PRIVILEGES")
    mydb.close()

# Function install PIP
def install_pip():
    os.system("sudo apt-get install python3-pip")

# Function install PHP-MySQL
def install_php():
    os.system("sudo apt-get install -y php-gd php-mysql")
    os.system("sudo systemctl restart apache2.service")

# Function install WordPress
def install_wordpress():
    os.chdir("/tmp")
    os.system("wget https://wordpress.org/latest.tar.gz")
    os.system("tar -zxf latest.tar.gz")

# Function configure WordPress
def config_wordpress():
    os.system("sudo rsync -avP /tmp/wordpress/ /var/www/html/")
    os.system("mkdir /var/www/html/wp-content/uploads")
    os.system("sudo chown -R www-data:www-data /var/www/html/")
    os.chdir("/var/www/html/")
    os.system("cp wp-config-sample.php wp-config.php")
    os.system("sudo chmod 646 wp-config.php")
    op_1 = open("/var/www/html/wp-config.php", "rt")
    re_1 = op_1.read()
    rep_1 = re.sub("database_name_here", str(dic["database_name"]), re_1)
    rep_2 = re.sub("username_here", str(dic["mariauser"]), rep_1)
    rep_3 = re.sub("password_here", str(dic["mariapass"]), rep_2)
    op_1.close()
    op_2 = open("/var/www/html/wp-config.php", "wt")
    op_2.write(rep_3)
    # Tidy up
    os.system("rm -Rf /tmp/wordpress")
    os.system("rm -f /tmp/latest.tar.gz")
    