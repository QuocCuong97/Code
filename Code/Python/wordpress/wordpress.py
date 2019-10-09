import re
import os
import json
import subprocess
# Function create Database
def creat_database():
    #op = open('settings.json')
    #rd = op.read()
    #data = json.dumps(rd)
    #print(data['mariahost'])
    global(mariadb) = "wordpress"
    global(mariauser) = "wordpressuser"
    global(mariapass) = "P@ssw0rd"
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
    os.system("sed -i -e "s/database_name_here/"$mariadb"/g" wp-config.php")
    os.system("sed -i -e "s/username_here/"$mariauser"/g" wp-config.php")
    os.system("sed -i -e "s/password_here/"$mariapass"/g" wp-config.php")
    # Tidy up
    os.system("rm -Rf /tmp/wordpress")
    os.system("rm -f /tmp/latest.tar.gz")
