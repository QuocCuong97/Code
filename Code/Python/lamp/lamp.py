import os
import re
import time
import subprocess
def start(service_name):
    os.system("sudo systemctl start %s" %service_name)
    print("%s started" %service_name)

def enable(service_name):
    os.system("sudo systemctl enable %s" %service_name)
    print("%s stopped" %service_name)

try:
    op = open("/etc/os-release", "rt")
    re_1 = op.read()
    sear_1 = re.search("Ubuntu", re_1)
    sear_2 = re.search("CentOS", re_1)
    if (sear_1):
        def install_apache2():
            os.system("echo 'P@ssw0rd' | sudo -S apt-get install apache2 -y")
            os.system("sudo ufw allow 'Apache'")
            start("apache2")
            enable("apache2")
            os.system('clear')
        def install_mariadb():
            os.system("sudo apt-get install software-properties-common")
            os.system("sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8")
            os.system("sudo add-apt-repository 'deb [arch=amd64,arm64,ppc64el] http://sfo1.mirrors.digitalocean.com/mariadb/repo/10.4/ubuntu bionic main'")
            os.system("sudo apt-get install -y mariadb-server mariadb-client")
            start("mariadb")
            enable("mariadb")
            os.system("clear")
        def install_php():
            os.system("sudo add-apt-repository ppa:ondrej/php")
            os.system("sudo apt-get install -y php7.3")
            os.system("clear")
        def check_ubuntu():
            ver_1 = subprocess.getoutput('cat /etc/os-release | grep "VERSION="')
            ver_2 = re.split("=", ver_1)
            ver_3 = ver_2[1]
            ver_4 = str(ver_3).strip('"')
            print("Ubuntu Version:", ver_4)
        def check_apache2():
            ver_1 = subprocess.getoutput("apache2 -v | grep Apache")
            ver_2 = re.split("\s", ver_1)
            ver_3 = str(ver_2[2])
            ver_4 = re.split("/", ver_3)
            ver = str(ver_4[1])
            status = subprocess.getoutput("sudo systemctl status apache2.service | grep 'active (running)'")
            if status:
                print("Apache Version:", ver, "----status:", "\033[1;32mactive (running)", "\033[0m")
            else:
                print("Apache Version:", ver, "----status:", "\033[1;32minactive (dead)", "\033[0m")
        def check_mariadb():
            ver_1 = subprocess.getoutput("mariadb -V")
            ver_2 = re.split("\s", ver_1)
            ver_3 = str(ver_2[5])
            ver_4 = re.split("-", ver_3)
            ver = str(ver_4[0])
            status = subprocess.getoutput("sudo systemctl status mariadb.service | grep 'active (running)'")
            if status:
                print("MariaDB Version:", ver, "----status:", "\033[1;32mactive (running)", "\033[0m")
            else:
                print("MariaDB Version:", ver, "----status:", "\033[1;32minactive (dead)", "\033[0m")
        def check_php():
            ver_1 = subprocess.getoutput("php -v | grep cli")
            ver_2 = re.split("\s", ver_1)
            ver_3 = ver_2[1]
            ver_4 = re.split("-", ver_3)
            ver = str(ver_4[0])
            print("PHP Version:", ver)
        os.system('clear')
        print("=========================================================================")
        print("******************LAMP Installation - Edited by Cuo**********************")
        print("=========================================================================")
        print("First Step: Install Apache 2")
        print("====================================")
        install_apache2()

        print("=========================================================================")
        print("Second Step: Install MariaDB 10.4.8")
        print("=======================================")
        install_mariadb()

        print("=========================================================================")
        print("Last Step: Install PHP 7.3")
        print("================================")
        install_php()

        print("=========================================================================")
        print("Install successfully , enjoy LAMP!")
        print("=========================================================================")
        time.sleep(5)
        x = input("Do you want to show LAMP status? [Y/n] ")
        if x in ["Y", "y", "Yes", "yes"]:
            check_ubuntu()
            check_apache2()
            check_mariadb()
            check_php()
        else:
            os.system("clear")
    elif (sear_2):
        def install_httpd():
            os.system('yum install -y httpd')
            start("httpd")
            enable("httpd")
            os.system('firewall-cmd --zone=public --permanent --add-service=http')
            os.system('firewall-cmd --reload')
            os.system('clear')
        def install_mariadb():
            os.system('echo "[mariadb]\nname = MariaDB\nbaseurl = http://yum.mariadb.org/10.4.8/centos7-amd64\ngpgkey=http://yum.mariadb.org/RPM-GPG-KEY-MariaDB\ngpgcheck=1" > /etc/yum.repos.d/MariaDB.repo')
            os.system('yum repolist')
            os.system('yum install MariaDB-server MariaDB-client MariaDB-devel -y')
            start("mariadb")
            enable("mariadb")
            os.system('clear')
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
        def check_centos():
            print(subprocess.getoutput('cat /etc/centos-release'))
        def check_httpd():
            ver_1 = subprocess.getoutput("httpd -v | grep Apache")
            ver_2 = re.split("\s", ver_1)
            ver_3 = str(ver_2[2])
            ver_4 = re.split("/", ver_3)
            ver = str(ver_4[1])
            status = subprocess.getoutput("systemctl status httpd | grep 'active (running)'")
            if status:
                print("Apache Version:", ver, "----status:", "\033[1;32mactive (running)", "\033[0m")
            else:
                print("Apache Version:", ver, "----status:", "\033[1;32minactive (dead)", "\033[0m")
        def check_mariadb():
            ver_1 = subprocess.getoutput("mariadb -V")
            ver_2 = re.split("\s", ver_1)
            ver_3 = str(ver_2[5])
            ver_4 = re.split("-", ver_3)
            ver = str(ver_4[0])
            status = subprocess.getoutput("systemctl status mariadb | grep 'active (running)'")
            if status:
                print("MariaDB Version:", ver, "----status:", "\033[1;32mactive (running)", "\033[0m")
            else:
                print("MariaDB Version:", ver, "----status:", "\033[1;32minactive (dead)", "\033[0m")
        def check_php():
            ver_1 = subprocess.getoutput("php -v | grep cli")
            ver_2 = re.split("\s", ver_1)
            ver = str(ver_2[1])
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
        os.system("rm -f remi-release-7.rpm*")

        print("=========================================================================")
        print("Install successfully , enjoy LAMP!")
        print("=========================================================================")
        time.sleep(5)
        x = input("Do you want to show LAMP status? [Y/n] ")
        if x in ["Y", "y", "Yes", "yes"]:
            check_centos()
            check_httpd()
            check_mariadb()
            check_php()
        else:
            os.system("clear")
except:
    print("OS not supported!")
