#!/bin/bash
install_httpd(){
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    firewall-cmd --zone=public --permanent --add-service=http
    firewall-cmd --reload
}

install_mariadb(){
    echo -e '[mariadb]\nname = MariaDB\nbaseurl=http://yum.mariadb.org/10.4.12/centos7-amd64\ngpgkey=http://yum.mariadb.org/RPM-GPG-KEY-MariaDB\ngpgcheck=1' > /etc/yum.repos.d/MariaDB.repo
    yum repolist
    yum install MariaDB-server MariaDB-client MariaDB-devel -y
    systemctl start mariadb.service
    systemctl enable mariadb.service
}

install_php(){
    yum install -y epel-release
    yum install -y yum-utils
    wget https://rpms.remirepo.net/enterprise/remi-release-7.rpm
    rpm -Uvh remi-release-7.rpm
    yum-config-manager --disable remi-php54
    yum-config-manager --enable remi-php74
    yum install php -y
    rm -f remi-release-7.rpm*
    echo -e'<?php\nphpinfo();\n?>' > /var/www/html/info.php
    systemctl restart httpd
}

check_centos(){
    my_string=$(cat /etc/centos-release)
    echo -e "$my_string"
}

check_httpd(){
    my_string=$(httpd -v)
    IFS=' ' read -ra raw_array <<< "$my_string"
    IFS='/' read -ra ver <<< "${raw_array[2]}"
    if [ -n "$(systemctl status httpd | grep 'active (running)')" ] 
    then
        echo -e "Apache Version: ${ver[1]} ----status: \033[1;32mactive (running)\033[0m"
    elif [ -n "$(systemctl status httpd | grep 'inactive (dead)')" ] 
    then
        echo -e "Apache Version: ${ver[1]} ----status: \033[1;31minactive (dead)\033[0m"
    else
        echo -e "Apache Version: ${ver[1]} ----status: \033[1;31mfailed\033[0m"
    fi
}

check_mariadb(){
    my_string=$(mariadb -V)
    IFS=' ' read -ra raw_array <<< "$my_string"
    IFS='-' read -ra ver <<< "${raw_array[4]}"
    if [ -n "$(systemctl status mariadb | grep 'active (running)')" ] 
    then
        echo -e "MariaDB Version: ${ver[0]} ----status: \033[1;32mactive (running)\033[0m"
    elif [ -n "$(systemctl status mariadb | grep 'inactive (dead)')" ] 
    then
        echo -e "MariaDB Version: ${ver[0]} ----status: \033[1;31minactive (dead)\033[0m"
    else
        echo -e "MariaDB Version: ${ver[0]} ----status: \033[1;31mfailed\033[0m"
    fi
}

check_php(){
    my_string=$(php -v | grep cli)
    IFS=' ' read -ra ver <<< "$my_string"
    echo -e "PHP Version: ${ver[1]}"
}

main(){
    clear
    printf "=========================================================================\n"
    printf "******************LAMP Installation - Edited by Cuo**********************\n"
    printf "=========================================================================\n"
    printf "First Step: Install Apache 2.4.6\n"
    printf "====================================\n"
    install_httpd

    clear
    printf "=========================================================================\n"
    printf "Second Step: Install MariaDB 10.4.12\n"
    printf "=======================================\n"
    install_mariadb

    clear
    printf "=========================================================================\n"
    printf "Last Step: Install PHP 7.4\n"
    printf "================================\n"
    install_php

    clear
    printf "=========================================================================\n"
    printf "Install successfully , enjoy LAMP! \n"
    printf "=========================================================================\n"
    sleep 5

    read -p "Do you want to show LAMP status? [Y/n]" choice
    case $choice in
        [yY][eE][sS]|[yY])
            check_centos
            check_httpd
            check_mariadb
            check_php
            ;;
        [nN][oO]|[nN])
            ;;
        *)
            echo "Sorry, invalid input..."
            ;;
    esac
}

main