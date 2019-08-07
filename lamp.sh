#!/bin/bash
clear
printf "=========================================================================\n"
printf "LAMP Installation - Edited by Cuo\n"
printf "=========================================================================\n"
printf "First Step: Install Apache 2.4.6\n"
printf "=========================================================================\n"

yum install -y httpd
systemctl start httpd
systemctl enable httpd
firewall-cmd --zone=public --permanent --add-service=http
firewall-cmd --reload
clear
printf "=========================================================================\n"
printf "Second Step: Install MariaDB 10.4.6\n"
printf "=========================================================================\n"
echo "[mariadb]
name = MariaDB
baseurl = http://yum.mariadb.org/10.4.6/centos7-amd64
gpgkey=http://yum.mariadb.org/RPM-GPG-KEY-MariaDB
gpgcheck=1" > /etc/yum.repos.d/MariaDB.repo
yum repolist
yum install MariaDB-server MariaDB-client MariaDB-devel -y
systemctl start mariadb.service
systemctl enable mariadb.service
clear
printf "=========================================================================\n"
printf "Last Step: Install PHP 7.3.7\n"
printf "=========================================================================\n"
yum install -y epel-release.noarch
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
printf "=========================================================================\n"
printf "Install successfully , enjoy LAMP! \n"
printf "=========================================================================\n"
