#!/bin/bash
# Cài đặt dịch vụ Web Server Apache
install_httpd(){
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    firewall-cmd --zone=public --permanent --add-service=http
    firewall-cmd --reload
}
# Cài đặt dịch vụ Database MariaDB
install_mariadb(){
echo "[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.4.7/centos7-amd64
gpgkey=http://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1" > /etc/yum.repos.d/MariaDB.repo
    yum repolist
    yum install MariaDB-server MariaDB-client MariaDB-devel -y
    systemctl start mariadb.service
    systemctl enable mariadb.service
}
# Cài đặt PHP
install_php(){
    yum install -y epel-release
    yum install -y yum-utils
    wget https://rpms.remirepo.net/enterprise/remi-release-7.rpm
    rpm -Uvh remi-release-7.rpm
    yum-config-manager --disable remi-php54
    yum-config-manager --enable remi-php73
    yum install php -y
    echo "<?php
    phpinfo();
    ?>" > /var/www/html/info.php
    systemctl restart httpd
}

clear
printf "=========================================================================\n"
printf "****************Script cài đặt LAMP Stack - Edited by Cuo****************\n"
printf "=========================================================================\n"
printf "Bước 1: Cài đặt Apache 2.4.6\n"
printf "====================================\n"
install_httpd

clear
printf "=========================================================================\n"
printf "Bước 2: Cài đặt MariaDB 10.4.7\n"
printf "=======================================\n"
install_mariadb

clear
printf "=========================================================================\n"
printf "Bước cuối cùng: Cài đặt PHP 7.3.8\n"
printf "================================\n"
install_php

printf "=========================================================================\n"
printf "Cài đặt LAMP Stack thành công trên node của bạn! \n"
printf "=========================================================================\n"
