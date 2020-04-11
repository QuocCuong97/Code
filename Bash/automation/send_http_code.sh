#!/bin/bash

WEB="https://price.supportdao.com"
SENDER="devtechnical024@gmail.com"
SENDER_PASS="Nhanhoa@001"
RECEIVER="thunderpassenger@gmail.com"

install_postfix(){
    yum remove sendmail*
    yum -y install postfix cyrus-sasl-plain mailx
    alternatives --set mta /usr/sbin/sendmail.postfix
    systemctl start postfix
    systemctl start postfix
}

configure_postfix(){
    echo "relayhost = [smtp.gmail.com]:587" >> /etc/postfix/main.cf
    echo "smtp_use_tls = yes" >> /etc/postfix/main.cf
    echo "smtp_sasl_auth_enable = yes" >> /etc/postfix/main.cf
    echo "smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd" >> /etc/postfix/main.cf
    echo "smtp_tls_CAfile = /etc/ssl/certs/ca-bundle.crt" >> /etc/postfix/main.cf
    echo "smtp_sasl_security_options = noanonymous" >> /etc/postfix/main.cf
    echo "smtp_sasl_tls_security_options = noanonymous" >> /etc/postfix/main.cf
}
    
configure_sender_mail(){
    echo "[smtp.gmail.com]:587 $1:$2" > /etc/postfix/sasl_passwd
    postmap /etc/postfix/sasl_passwd
    chown root:postfix /etc/postfix/sasl_passwd*
    chmod 640 /etc/postfix/sasl_passwd*
    systemctl reload postfix
}

send_mail(){
    http_code_raw=$(curl -I -s $1 | grep HTTP)
    IFS=' ' read -ra raw_array <<< "$http_code_raw"
    message="Website '$1' - Status Code: ${raw_array[1]}"
    echo $message | mail -s "HTTP Status Code" $2
}

setup_cron(){
    _self="${0##*/}"
    CRON="$PWD/$_self"
    if [ -z "$(cat /etc/crontab | grep $CRON)" ]
    then
        yum install -y cronie
        service crond start
        systemctl enable crond
        echo "*/5 * * * * root $CRON" >> /etc/crontab
    fi
}

install_postfix
configure_postfix
configure_sender_mail $SENDER $SENDER_PASS
send_mail $WEB $RECEIVER
setup_cron