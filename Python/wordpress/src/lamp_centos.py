import os
import re
import subprocess
from . import operate_service

# Funcion install HTTPD
def install_httpd():
    os.system('yum install -y httpd')
    operate_service.start("httpd")
    operate_service.enable("httpd")
    operate_service.firewalld("httpd")
    os.system('clear')

# Function install MariaDB
def install_mariadb():
    os.system('echo "[mariadb]\nname = MariaDB\nbaseurl = http://yum.mariadb.org/10.4.8/centos7-amd64\ngpgkey=http://yum.mariadb.org/RPM-GPG-KEY-MariaDB\ngpgcheck=1" > /etc/yum.repos.d/MariaDB.repo')
    os.system('yum repolist')
    os.system('yum install MariaDB-server MariaDB-client MariaDB-devel -y')
    operate_service.start("mariadb")
    operate_service.enable("mariadb")
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
    get_raw = subprocess.getoutput("httpd -v | grep Apache")
    split_1 = re.split("\s", get_raw)
    lst = str(split_1[2])
    split_2 = re.split("/", lst)
    ver = str(split_2[1])
    stt = subprocess.getoutput("systemctl status httpd | grep 'active (running)'")
    if stt:
        print("Apache Version:", ver, "----status:", "\033[1;32mactive (running)", "\033[0m")
    else:
        print("Apache Version:", ver, "----status:", "\033[1;32minactive (dead)", "\033[0m")

# Function check status mariadb
def check_mariadb():
    get_raw = subprocess.getoutput("mariadb -V")
    split_1 = re.split("\s", get_raw)
    lst = str(split_1[5])
    split_2 = re.split("-", lst)
    ver = str(split_2[0])
    stt = subprocess.getoutput("systemctl status mariadb | grep 'active (running)'")
    if stt:
        print("MariaDB Version:", ver, "----status:", "\033[1;32mactive (running)", "\033[0m")
    else:
        print("MariaDB Version:", ver, "----status:", "\033[1;32minactive (dead)", "\033[0m")

# Function check status PHP
def check_php():
    get_raw = subprocess.getoutput("php -v | grep cli")
    sp_lit = re.split("\s", get_raw)
    ver = str(sp_lit[1])
    print("PHP Version:", ver)

