#!/bin/bash
## Secure SSH on CentOS 7
DIRECTORY=$(cd `dirname $0` && pwd)
change_port_number(){
    echo -n "Change default port (22) for SSH? [Y/n] "
    read ans
    if [ "$ans" = "Y" ] 
    then
        echo -n "Which port do you want? "
        read port
        sed -i -e "s/\#Port 22/Port $port/g" /etc/ssh/sshd_config
    else
        echo -n "Nothing changed!\n"
    fi
}
disable_root_login(){
    echo -n "Disable root login? [Y/n] "
    read ans
    if [ "$ans" = "Y" ] 
    then
    sed -i -e "s/\#PermitRootLogin yes/PermitRootLogin no/g" /etc/ssh/sshd_config
    else
        echo -n "Nothing changed! \n"
    fi
}
max_auth_tries(){
    echo -n "Maximum authentication attempts : "
    read ans
    if [ "$ans" = "" ] 
    then
        echo -n "Nothing changed! \n"
    else
        sed -i -e "s/\#MaxAuthTries 6/MaxAuthTries $ans/g" /etc/ssh/sshd_config
    fi
}
max_sessions(){
    echo -n "Maximum SSH sessions : "
    read ans
    if [ "$ans" = "" ] 
    then
        echo -n "Nothing changed! \n"
    else
        sed -i -e "s/\#MaxSessions 10/MaxSessions $ans/g" /etc/ssh/sshd_config
    fi    
}
disable_password(){
    echo -n "Disable password-based authentication (Public-Key instead)? [Y/n] "
    read ans
    if [ "$ans" = "Y" ] 
    then
    sed -i -e "s/\#PubkeyAuthentication yes/PubkeyAuthentication yes/g" /etc/ssh/sshd_config
    sed -i -e "s/\#PasswordAuthentication yes/PasswordAuthentication no/g" /etc/ssh/sshd_config
    else
        echo -n "Nothing changed! \n"
    fi
}
change_port_number
disable_root_login
disable_password
max_auth_tries
max_sessions
systemctl restart sshd
# Script sẽ được bổ sung thêm các tùy chọn khác....
