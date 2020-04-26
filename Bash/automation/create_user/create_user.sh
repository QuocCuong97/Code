#!/bin/bash

INPUT_FILE='list.csv'
i=0
while read -r line;do
    username[$i]=$(echo $line | awk -F ',' '{print $1}')
    domain[$i]=$(echo $line | awk -F ',' '{print $2}')
    password[$i]=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1)
    i=$(($i+1))
done < $INPUT_FILE
echo ${username[1]}
echo 'USER  DOMAIN  PASSWORD' > $INPUT_FILE
for (( x=1 ; x<i ; x++ ))
do
    echo -e "${username[$x]},${domain[$x]},${password[$x]}" >> $INPUT_FILE
    # sudo prosodyctl register ${username[$x]} ${domain[$x]} ${password[$x]}
done
echo "Đã tạo $(($i-1)) tài khoản"
