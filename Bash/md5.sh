#!/bin/bash
echo -n "$2's password:"
read -s pass
touch /root/code/md5_src
if [ -f $1 ];then
    sshpass -p $pass scp $1 $2:$3
    md5sum $1 >> md5_src
    sshpass -p $pass ssh $2 "md5sum $3/$(basename $1) >> $3/md5_dst"
else 
    sshpass -p $pass scp -r $1 $2:$3
    FILES=$1/*
    for file in $FILES;do
        if [ -f $file ];then
            md5sum $file >> md5_src
            sshpass -p $pass ssh $2 "/usr/bin/md5sum $3/$(basename $file) >> $3/md5_dst"
        fi
    done
fi
cat md5_src | awk '{print $1}' >| md5_src.txt
rm -f md5_src
#sshpass -p $pass ssh $2 "cat $3/md5_dst | awk '{print $1}' >| md5_dst.txt"

#ssh user@remote_host "cat $1/md5_dst.md5" | diff -q - md5_src.md5.txt
echo "\n"