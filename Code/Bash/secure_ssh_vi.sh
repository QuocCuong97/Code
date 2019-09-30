#!/bin/bash
## Secure SSH on CentOS 7
DIRECTORY=$(cd `dirname $0` && pwd)
# Thay đổi Port LISTEN mặc định
change_port_number(){
    echo -n "Thay đổi port mặc định (22) của SSH? [Y/n] "
    read ans
    if [ "$ans" = "Y" ] 
    then
        echo -n "Bạn muốn đổi thành port nào? "
        read port
        sed -i -e "s/\#Port 22/Port $port/g" /etc/ssh/sshd_config
    else
        echo -n "Không có gì thay đổi!\n"
    fi
}
# Không cho đăng nhập bằng user root
disable_root_login(){
    echo -n "Khóa đăng nhập bằng user root? [Y/n] "
    read ans
    if [ "$ans" = "Y" ] 
    then
    sed -i -e "s/\#PermitRootLogin yes/PermitRootLogin no/g" /etc/ssh/sshd_config
    else
        echo -n "Không có gì thay đổi! \n"
    fi
} 
# Thiết lập số lần đăng nhập sai tối đa
max_auth_tries(){
    echo -n "Số lần đăng nhập sai tối đa cho phép: "
    read ans
    if [ "$ans" = "" ] 
    then
        echo -n "Không có gì thay đổi! \n"
    else
        sed -i -e "s/\#MaxAuthTries 6/MaxAuthTries $ans/g" /etc/ssh/sshd_config
    fi
}
# Thiết lập số phiên đăng nhập SSH tối đa
max_sessions(){
    echo -n "Số phiên đăng nhập SSH tối đa cho phép: "
    read ans
    if [ "$ans" = "" ] 
    then
        echo -n "Không có gì thay đổi! \n"
    else
        sed -i -e "s/\#MaxSessions 10/MaxSessions $ans/g" /etc/ssh/sshd_config
    fi    
}
# Sử dụng chứng thực bằng SSH key , thay vì mật khẩu
disable_password(){
    echo -n "Sử dụng chứng thực bằng SSH key , thay vì mật khẩu? [Y/n] "
    read ans
    if [ "$ans" = "Y" ] 
    then
    sed -i -e "s/\#PubkeyAuthentication yes/PubkeyAuthentication yes/g" /etc/ssh/sshd_config
    sed -i -e "s/\#PasswordAuthentication yes/PasswordAuthentication no/g" /etc/ssh/sshd_config
    else
        echo -n "Không có gì thay đổi! \n"
    fi
}
change_port_number
disable_root_login
disable_password
max_auth_tries
max_sessions
systemctl restart sshd
# Script sẽ được bổ sung thêm các tùy chọn khác....
