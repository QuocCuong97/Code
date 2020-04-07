#!/bin/bash
## Install Wordpress on CentOS7
DIRECTORY=$(cd `dirname $0` && pwd)
create_database(){
    echo -n "MariaDB Host (localhost): "
    read mariahost
    if [ "$mariahost" = "" ]
    then
	mariahost="localhost"
    fi
    echo -n "New MariaDB Name: "
    read mariadb

    echo -n "New MariaDB User: "
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
install_php(){
    yum install -y php-gd php-mysql
    systemctl restart httpd
}
install_wordpress(){
    cd /tmp
    wget http://wordpress.org/latest.tar.gz
    tar -zxf latest.tar.gz
}
config_wordpress(){
    rsync -avP /tmp/wordpress/ /var/www/html/
    mkdir /var/www/html/wp-content/uploads
    chown -R apache:apache /var/www/html/
    cd /var/www/html/
    cp wp-config-sample.php wp-config.php
    sed -i -e "s/database_name_here/$mariadb/g" wp-config.php
    sed -i -e "s/username_here/"$mariauser"/g" wp-config.php
    sed -i -e "s/password_here/"$mariapass"/g" wp-config.php
    # Tidy up
    rm -Rf /tmp/wordpress
    rm -f /tmp/latest.tar.gz
}
check_wordpress(){
    ver=$(grep wp_version /var/www/html/wp-includes/version.php | awk -F "'" '{print $2}')
    echo -e "WordPress Version: ${ver}"
}

clear
printf "=========================================================================\n"
printf "*********WordPress Installation on CentOS 7 - Edited by Cuo**************\n"
printf "=========================================================================\n"
printf "First Step: Creat Database\n"
printf "==============================\n"
create_database

clear
printf "=========================================================================\n"
printf "Second Step: Download some PHP modules \n"
printf "===========================================\n"
install_php

clear
printf "=========================================================================\n"
printf "Third Step: Download the lastest version of WordPress \n"
printf "==========================================================\n"
install_wordpress

clear
printf "=========================================================================\n"
printf "Last Step: Configuration \n"
printf "=============================\n"
config_wordpress

clear
printf "=========================================================================\n"
printf "Install successfully , enjoy WordPress! \n"
printf "=========================================================================\n"

sleep 5

read -p "Do you want to show WordPress's version? [Y/n]" choice
case $choice in
    [yY][eE][sS]|[yY])
        check_wordpress
        ;;
    [nN][oO]|[nN])
        ;;
    *)
        echo "Sorry, invalid input..."
        ;;
esac
