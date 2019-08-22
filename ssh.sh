#!/bin/bash
## Secure SSH on CentOS 7
DIRECTORY=$(cd `dirname $0` && pwd)
change_port_number(){
    echo -n "Do you want to change default port (22) for SSH? (Y/n)"
    read ans1
    if [ $ans1 eq Y ] 
    then
        echo -n "Which port do you want?"
        read port
        sed -i -e "s/"\#Port 22"/"Port "$port""/g" /etc/ssh/sshd_config
    else
        echo -n "Nothing changed!"
    fi
}
change_port_number()