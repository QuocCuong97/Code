import os
import re
import subprocess
from src import operate_service

try:
    os_name = operate_service.check_os()
    if os_name == "Ubuntu":
        check_apache2 = os.path.exists("/lib/systemd/system/apache2.service")
        if check_apache2 == False:
            from src import lamp_ubuntu
            lamp_ubuntu.install_apache2()
        else:
            pass
        check_mariadb = os.path.exists("/lib/systemd/system/mariadb.service")
        if check_mariadb == False:
            from src import lamp_ubuntu
            lamp_ubuntu.install_mariadb()
        else:
            pass
        check_php = os.path.exists("/usr/bin/php")
        if check_php == False:
            from src import lamp_ubuntu
            lamp_ubuntu.install_php()
        else:
            pass
        from src import wordpress_ubuntu
        os.system("clear")
        print("=========================================================================")
        print("*********WordPress Installation on Ubuntu - Edited by Cuo**************")
        print("=========================================================================")
        print("First Step: Connect Database")
        print("==============================")
        wordpress_ubuntu.read_info()
        wordpress_ubuntu.install_pip()
        wordpress_ubuntu.creat_database()

        os.system("clear")
        print("=========================================================================")
        print("Second Step: Download some PHP modules")
        print("===========================================")
        wordpress_ubuntu.install_php()

        os.system("clear")
        print("=========================================================================")
        print("Third Step: Download the lastest version of WordPress")
        print("==========================================================")
        wordpress_ubuntu.install_wordpress()

        os.system("clear")
        print("=========================================================================")
        print("Last Step: Configuration")
        print("=============================")
        wordpress_ubuntu.config_wordpress()

        os.system("clear")
        print("=========================================================================")
        print("Install successfully , enjoy WordPress!")
        print("=========================================================================")
    elif os_name == "CentOS":
        check_httpd = os.path.exists("/lib/systemd/system/httpd.service")
        if check_httpd == False:
            from src import lamp_centos
            lamp_centos.install_httpd()
        else:
            pass
        check_mariadb = os.path.exists("/lib/systemd/system/mariadb.service")
        if check_mariadb == False:
            from src import lamp_centos
            lamp_centos.install_mariadb()
        else:
            pass
        check_php = os.path.exists("/usr/bin/php")
        if check_php == False:
            from src import lamp_centos
            lamp_centos.install_php()
        else:
            pass
        from src import wordpress_centos
        os.system("clear")
        print("=========================================================================")
        print("*********WordPress Installation on CentOS 7 - Edited by Cuo**************")
        print("=========================================================================")
        print("First Step: Connect Database")
        print("==============================")
        wordpress_centos.read_info()
        wordpress_centos.install_pip()
        wordpress_centos.creat_database()

        os.system("clear")
        print("=========================================================================")
        print("Second Step: Download some PHP modules")
        print("===========================================")
        wordpress_centos.install_php()

        os.system("clear")
        print("=========================================================================")
        print("Third Step: Download the lastest version of WordPress")
        print("==========================================================")
        wordpress_centos.install_wordpress()

        os.system("clear")
        print("=========================================================================")
        print("Last Step: Configuration")
        print("=============================")
        wordpress_centos.config_wordpress()

        os.system("clear")
        print("=========================================================================")
        print("Install successfully , enjoy WordPress!")
        print("=========================================================================")
    else:
        print("OS not supported!")
except:
    print("OS not supported!")



    
