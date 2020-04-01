#!/bin/bash

install_nginx(){
    echo -e '[nginx]\nname=nginx repo\nbaseurl=http://nginx.org/packages/centos/7/$basearch/\n\ngpgcheck=1' > /etc/yum.repos.d/nginx.repo
    yum install -y wget
    wget --no-check-certificate -O nginx_signing.key https://nginx.org/keys/nginx_signing.key
    rpm --import nginx_signing.key
    yum repolist
    yum --disablerepo=* --enablerepo=nginx install nginx -y
    firewall-cmd --zone=public --permanent --add-port=80/tcp
    firewall-cmd --zone=public --permanent --add-port=443/tcp
    firewall-cmd --reload
    rm -f nginx_signing.key
    systemctl start nginx.service
    systemctl enable nginx.service
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

check_nginx(){
    my_string=$(nginx -v)
    IFS='/' read -ra ver <<< "$my_string"
    # if [ -n "$(systemctl status nginx | grep 'active (running)')" ] 
    # then
    #     echo -e "NGINX Version: ${ver[1]} ----status: \033[1;32mactive (running)\033[0m"
    # elif [ -n "$(systemctl status httpd | grep 'inactive (dead)')" ] 
    # then
    #     echo -e "NGINX Version: ${ver[1]} ----status: \033[1;31minactive (dead)\033[0m"
    # else
    #     echo -e "NGINX Version: ${ver[1]} ----status: \033[1;31mfailed\033[0m"
    # fi
    if [ -n "$(systemctl status nginx | grep 'active (running)')" ] 
    then
        echo -e "NGINX Version: ----status: \033[1;32mactive (running)\033[0m"
    elif [ -n "$(systemctl status httpd | grep 'inactive (dead)')" ] 
    then
        echo -e "NGINX Version: ----status: \033[1;31minactive (dead)\033[0m"
    else
        echo -e "NGINX Version: ----status: \033[1;31mfailed\033[0m"
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
    printf "******************LEMP Installation - Edited by Cuo**********************\n"
    printf "=========================================================================\n"
    printf "First Step: Install NGINX\n"
    printf "============================\n"
    install_nginx

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
    printf "Install successfully , enjoy LEMP! \n"
    printf "=========================================================================\n"
    sleep 5

    read -p "Do you want to show LEMP status? [Y/n]" choice
    case $choice in
        [yY][eE][sS]|[yY])
            check_centos
            check_nginx
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