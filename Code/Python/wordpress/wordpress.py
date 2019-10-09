import re
import os
import subprocess
def creat_database():
    mariahost = input('MariaDB Host (localhost): ')
    if mariahost == '':
        mariahost == 'localhost'
    mariadb = input('New MariaDB Name: ')
    mariauser = input('New MariaDB User: ')
    mariapass = input('Password: ')

# Function install some PHP packages
def install_php():
    os.system("yum install -y php-gd php-mysql")
    os.system("systemctl restart httpd")

# Function install WordPress
def install_wordpress():
    os.system("cd /tmp")
    os.system("yum install -y wget")
    os.system("wget http://wordpress.org/latest.tar.gz")
    os.system("tar -zxf latest.tar.gz")

# Configure WordPress
def config_wordpress():
    os.system("rsync -avP /tmp/wordpress/ /var/www/html/")
    os.system("mkdir /var/www/html/wp-content/uploads")
    os.system("chown -R apache:apache /var/www/html/")
    os.system("cd /var/www/html/")
    os.system("cp wp-config-sample.php wp-config.php")
    os.system("sed -i -e "s/database_name_here/$mariadb/g" wp-config.php")
    os.system("sed -i -e "s/username_here/"$mariauser"/g" wp-config.php")
    os.system("sed -i -e "s/password_here/"$mariapass"/g" wp-config.php")
    # Tidy up
    
