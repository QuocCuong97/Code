#!/bin/bash

# Script install Agent for Backup Service

check_distribution(){
    distribution_raw=$(cat /etc/os-release | grep ID_LIKE)
    # For Ubuntu/Debian
    if [[ $distribution_raw == *debian* ]] ; then
        sudo apt-get update -y
        sudo apt-get install -y jq curl
        echo "support"
    # For CentOS/RHEL 6,7,8
    elif [[ $distribution_raw == *rhel* || -f "/etc/redhat-release" ]] ; then                       
        yum install -y jq curl
        echo "support"
    else
        echo "not support"
    fi
}

get_lastest_download_url(){
    lastest_version=$(curl -X GET -s https://api.github.com/repos/bizflycloud/bizfly-backup/releases/latest | jq '.assets')
    length=$(echo $lastest_version | jq '. | length')
    arch=$(uname -m)
    if [[ $arch == x86_64 ]] ; then
        filename="bizfly-backup_linux_amd64.tar.gz"
    elif [[ $arch == i386 ]] ; then
        filename="bizfly-backup_linux_386.tar.gz"
    elif [[ $arch == arm ]] ; then
        filename="bizfly-backup_linux_arm64.tar.gz"
    else
        filename=""
    fi
    if [ -z "$filename" ]; then
        echo "not support"
    else
        i=0
        while [ $i -lt $length ]
        do  
            download_url_raw=$(echo $lastest_version | jq -r .[$i].browser_download_url)
            if [[ $download_url_raw == *$filename* ]]; then
                download_url=$download_url_raw
                break
            fi
            i=$(( $i + 1 ))
        done
    fi
    echo $download_url
}

install_agent(){
    if [[ $(check_distribution) == "not support" ]]; then
        echo "Not support!"
    else
        if [[ $(get_lastest_download_url) == "not support" ]]; then
            echo "Not support!"
        else
            curl -Ls $(get_lastest_download_url) --output "bizfly-backup.tar.gz"
            tar -xzf bizfly-backup.tar.gz
            mv bizfly /usr/bin
            rm -f bizfly-backup.tar.gz
        fi
    fi
}

run_agent_with_systemd(){
    cat <<EOF > /etc/agent.yaml
access_key: $ACCESS_KEY
api_url: $API_URL
machine_id: $MACHINE_ID
secret_key: $SECRET_KEY
EOF
    cat <<EOF > /etc/systemd/system/backup-agent.service
[Unit]
Description=Backup Agent Service

[Service]
Type=simple
ExecStart=/usr/bin/bizfly agent --config=/etc/agent.yaml

[Install]
WantedBy=multi-user.target
EOF
    sudo chmod 644 /etc/systemd/system/backup-agent.service
    systemctl enable backup-agent
    systemctl start backup-agent
    systemctl status backup-agent
}

clear
printf "=========================================================================\n"
printf "******************Backup Agent Installation - VCCloud********************\n"
printf "=========================================================================\n"
printf "First Step: Install Agent\n"
printf "====================================\n"
install_agent

clear
printf "=========================================================================\n"
printf "Second Step: Run Agent\n"
printf "=======================================\n"
run_agent_with_systemd ACCESS_KEY API_URL MACHINE_ID SECRET_KEY

### Usage
# ACCESS_KEY=OLIQSJ5EQKTRVB01HXJ0 \
# API_URL=https://dev.bizflycloud.vn/api/cloud-backup \
# MACHINE_ID=4a10ed55-812e-429b-a889-877ecae7088d \
# SECRET_KEY=66c1e87000944fd38eaa14f88bbcb310e5888c5fa58d44bba18ca2a2af9cd3a2 \
# bash backup-agent.sh

# OR
# ACCESS_KEY=OLIQSJ5EQKTRVB01HXJ0 \
# API_URL=https://dev.bizflycloud.vn/api/cloud-backup \
# MACHINE_ID=4a10ed55-812e-429b-a889-877ecae7088d \
# SECRET_KEY=791bc1fac71cef7acb77a4cb306352a5266ffe5f0749c8525d0cffd36c6c4207 \
# bash -c "$(curl -sSL https://raw.githubusercontent.com/QuocCuong97/Code/master/Bash/install_agent.sh)"