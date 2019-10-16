#!/bin/bash
## Install Wordpress on CentOS7
DIRECTORY=$(cd `dirname $0` && pwd)
# Khởi tạo Database cho WordPress
create_database(){
    echo -n "MariaDB Host (localhost): "
    read mariahost
    if [ "$mysqlhost" = "" ]
    then
	mariahost="localhost"
    fi
    echo -n "Nhập tên Database : "
    read mariadb

    echo -n "Nhập user sử dụng cho Database: "
    read mariauser

    echo -n "Password: "
    read mariapass

mysql -u root <<EOF
CREATE DATABASE $mariadb;
CREATE USER $mariauser@$mariahost IDENTIFIED BY '$mariapass';
GRANT ALL PRIVILEGES ON $mariadb.* TO $mariauser IDENTIFIED BY '$mariapass';
FLUSH PRIVILEGES;
exit;
EOF
}
# Cài đặt một số module PHP cần thiết
install_php(){
    yum install -y php-gd php-mysql
    systemctl restart httpd
}
# Tải về phiên bản mới nhất của WordPress
install_wordpress(){
    cd /tmp
    wget http://wordpress.org/latest.tar.gz
    tar -zxf latest.tar.gz
}
# Cấu hình WordPress
config_wordpress(){
    rsync -avP /tmp/wordpress/ /var/www/html/
    mkdir /var/www/html/wp-content/uploads
    chown -R apache:apache /var/www/html/
    cd /var/www/html/
    cp wp-config-sample.php wp-config.php
    sed -i -e "s/database_name_here/$mariadb/g" wp-config.php
    sed -i -e "s/username_here/"$mariauser"/g" wp-config.php
    sed -i -e "s/password_here/"$mariapass"/g" wp-config.php
    # Xóa file đã download
    rm -Rf /tmp/wordpress
    rm -f /tmp/latest.tar.gz
}
clear
printf "=========================================================================\n"
printf "*********Script cài đặt WordPress trên CentOS 7 - Edited by Cuo**************\n"
printf "=========================================================================\n"
printf "Bước 1: Khởi tạo Database\n"
printf "==============================\n"
create_database

clear
printf "=========================================================================\n"
printf "Bước 2: Download một số module PHP cần thiết \n"
printf "===========================================\n"
install_php

clear
printf "=========================================================================\n"
printf "Bước 3: Download phiên bản mới nhất của WordPress \n"
printf "==========================================================\n"
install_wordpress

clear
printf "=========================================================================\n"
printf "Last Step: Configuration \n"
printf "=============================\n"
config_wordpress

clear
printf "=========================================================================\n"
printf "Cài đặt WordPress thành công! \n"
printf "=========================================================================\n"