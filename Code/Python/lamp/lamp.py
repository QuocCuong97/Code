import os
import re
import subprocess

# Funcion install HTTPD
def install_httpd():
    os.system('yum install -y httpd')
    os.system('systemctl start httpd')
    os.system('systemctl enable httpd')
    os.system('firewall-cmd --zone=public --permanent --add-service=http')
    os.system('firewall-cmd --reload')
    os.system('clear')

# Function install MariaDB
def install_mariadb():
    os.system('echo "[mariadb]\nname = MariaDB\nbaseurl = http://yum.mariadb.org/10.4.8/centos7-amd64\ngpgkey=http://yum.mariadb.org/RPM-GPG-KEY-MariaDB\ngpgcheck=1" > /etc/yum.repos.d/MariaDB.repo')
    os.system('yum repolist')
    os.system('yum install MariaDB-server MariaDB-client MariaDB-devel -y')
    os.system('systemctl start mariadb.service')
    os.system('systemctl enable mariadb.service')
    os.system('clear')

# Function install PHP
def install_php():
    os.system('yum install -y epel-release')
    os.system('yum install -y yum-utils')
    os.system('yum install -y wget')
    os.system('wget https://rpms.remirepo.net/enterprise/remi-release-7.rpm')
    os.system('rpm -Uvh remi-release-7.rpm')
    os.system('yum-config-manager --disable remi-php54')
    os.system('yum-config-manager --enable remi-php73')
    os.system('yum install php -y')
    os.system('clear')

# Function check version CentOS
def check_centos():
    print(subprocess.getoutput('cat /etc/centos-release'))

# Function check status httpd
def check_httpd():
    a = subprocess.getoutput("httpd -v | grep Apache")
    b = re.split("\s", a)
    c = str(b[2])
    d = re.split("/", c)
    ver = str(d[1])
    stt = subprocess.getoutput("systemctl status httpd | grep 'active (running)'")
    if stt:
        print("Apache Version:", ver, "----status: active (running)")
    else:
        print("Apache Version:", ver, "----status: inactive (dead)")

# Function check status mariadb
def check_mariadb():
    a = subprocess.getoutput("mariadb -V")
    b = re.split("\s", a)
    c = str(b[5])
    d = re.split("-", c)
    ver = str(d[0])
    stt = subprocess.getoutput("systemctl status mariadb | grep 'active (running)'")
    if stt:
        print("MariaDB Version:", ver, "----status: active (running)")
    else:
        print("MariaDB Version:", ver, "----status: inactive (dead)")

# Function check status PHP
def check_php():
    a = subprocess.getoutput("php -v | grep cli")
    b = re.split("\s", a)
    ver = str(b[1])
    print("PHP Version:", ver)

os.system('clear')
print("=========================================================================")
print("******************LAMP Installation - Edited by Cuo**********************")
print("=========================================================================")
print("First Step: Install Apache 2.4.6")
print("====================================")
install_httpd()

print("=========================================================================")
print("Second Step: Install MariaDB 10.4.8")
print("=======================================")
install_mariadb()

print("=========================================================================")
print("Last Step: Install PHP 7.3")
print("================================")
install_php()
os.system("rm -f remi-release-7.rpm*")     # Clean-up

print("=========================================================================")
print("Install successfully , enjoy LAMP!")
print("=========================================================================")

x = input("Do you want to show LAMP status? [Y/n] ")
if x in ["Y", "y", "Yes", "yes"]:
    check_centos()
    check_httpd()
    check_mariadb()
    check_php()
else:
    os.system("clear")