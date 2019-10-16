import os
import re
import subprocess
from . import operate_service

# Funcion install Apache2
def install_apache2():
    os.system("echo 'P@ssw0rd' | sudo -S apt-get install apache2 -y")
    os.system("sudo ufw allow 'Apache'")
    operate_service.start("apache2")
    operate_service.enable("apache2")
    os.system('clear')

# Function install MariaDB
def install_mariadb():
    os.system("sudo apt-get install software-properties-common")
    os.system("sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8")
    os.system("sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.4/ubuntu bionic main'")
    os.system("sudo apt-get install -y mariadb-server mariadb-client")
    operate_service.start("mariadb")
    operate_service.enable("mariadb")
    os.system("clear")

# Function install PHP
def install_php():
    os.system("sudo add-apt-repository ppa:ondrej/php")
    os.system("sudo apt-get install -y php7.3")
    os.system("clear")

# Function check version Ubuntu
def check_ubuntu():
    get_raw = subprocess.getoutput('cat /etc/os-release | grep "VERSION="')
    sp_lit = re.split("=", get_raw)
    lst = sp_lit[1]
    ver = str(lst).strip('"')
    print("Ubuntu Version:", ver)

def check_apache2():
    get_raw = subprocess.getoutput("apache2 -v | grep Apache")
    split_1 = re.split("\s", get_raw)
    lst = str(split_1[2])
    split_2 = re.split("/", lst)
    ver = str(split_2[1])
    status = subprocess.getoutput("sudo systemctl status apache2.service | grep 'active (running)'")
    if status:
        print("Apache Version:", ver, "----status:", "\033[1;32mactive (running)", "\033[0m")
    else:
        print("Apache Version:", ver, "----status:", "\033[1;32minactive (dead)", "\033[0m")

def check_mariadb():
    get_raw = subprocess.getoutput("mariadb -V")
    split_1 = re.split("\s", get_raw)
    lst = str(split_1[5])
    split_2 = re.split("-", lst)
    ver = str(split_2[0])
    status = subprocess.getoutput("sudo systemctl status mariadb.service | grep 'active (running)'")
    if status:
        print("MariaDB Version:", ver, "----status:", "\033[1;32mactive (running)", "\033[0m")
    else:
        print("MariaDB Version:", ver, "----status:", "\033[1;32minactive (dead)", "\033[0m")

def check_php():
    get_raw = subprocess.getoutput("php -v | grep cli")
    split_1 = re.split("\s", get_raw)
    lst = split_1[1]
    split_2 = re.split("-", lst)
    ver = str(split_2[0])
    print("PHP Version:", ver)