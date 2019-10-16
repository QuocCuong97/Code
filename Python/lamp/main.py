import os
import time
from src import check_os

os_name = check_os()
if os_name == "Ubuntu":
    from src import lamp_ubuntu
    os.system('clear')
    print("=========================================================================")
    print("******************LAMP Installation - Edited by Cuo**********************")
    print("=========================================================================")
    print("First Step: Install Apache 2")
    print("====================================")
    lamp_ubuntu.install_apache2()

    print("=========================================================================")
    print("Second Step: Install MariaDB 10.4.8")
    print("=======================================")
    lamp_ubuntu.install_mariadb()

    print("=========================================================================")
    print("Last Step: Install PHP 7.3")
    print("================================")
    lamp_ubuntu.install_php()

    print("=========================================================================")
    print("Install successfully , enjoy LAMP!")
    print("=========================================================================")

    x = input("Do you want to show LAMP status? [Y/n] ")
    if x in ["Y", "y", "Yes", "yes"]:
        lamp_ubuntu.check_ubuntu()
        lamp_ubuntu.check_apache2()
        lamp_ubuntu.check_mariadb()
        lamp_ubuntu.check_php()
    else:
        os.system("clear")

elif os_name == "CentOS":
    from src import lamp_centos
    os.system('clear')
    print("=========================================================================")
    print("******************LAMP Installation - Edited by Cuo**********************")
    print("=========================================================================")
    print("First Step: Install Apache 2.4.6")
    print("====================================")
    lamp_centos.install_httpd()

    print("=========================================================================")
    print("Second Step: Install MariaDB 10.4.8")
    print("=======================================")
    lamp_centos.install_mariadb

    print("=========================================================================")
    print("Last Step: Install PHP 7.3")
    print("================================")
    lamp_centos.install_php()
    os.system("rm -f remi-release-7.rpm*")

    print("=========================================================================")
    print("Install successfully , enjoy LAMP!")
    print("=========================================================================")

    time.sleep(5)
    x = input("Do you want to show LAMP status? [Y/n] ")
    if x in ["Y", "y", "Yes", "yes"]:
        lamp_centos.check_centos()
        lamp_centos.check_httpd()
        lamp_centos.check_mariadb()
        lamp_centos.check_php()
    else:
        os.system("clear")

else:
    print("OS not supported!")

