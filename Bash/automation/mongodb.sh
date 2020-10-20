#!/bin/bash

install_mongodb(){
    echo -e "[mongodb-org-4.4]\nname=MongoDB Repository\nbaseurl=https://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/4.4/x86_64/\ngpgcheck=1\nenabled=1\ngpgkey=https://www.mongodb.org/static/pgp/server-4.4.asc" > /etc/yum.repos.d/mongodb-org-4.4.repo
    yum repolist
    yum install -y mongodb-org
    systemctl enable mongod
    systemctl start mongod
    systemctl status mongod
}

install_mongodb