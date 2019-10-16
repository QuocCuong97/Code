import os
import re
def start(service_name):
    os.system("sudo systemctl start %s" %service_name)
    print("%s started" %service_name)
def stop(service_name):
    os.system("sudo systemctl stop %s" %service_name)
    print("%s stopped" %service_name)
def status(service_name):
    os.system("sudo systemctl status %s" %service_name)
def check_os():
    op = open("/etc/os-release", "rt")
    re_1 = op.read()
    sear_1 = re.search("CentOS", re_1)
    sear_2 = re.search("Ubuntu", re_1)
    if (sear_1):
        return "CentOS"
    elif (sear_2):
        return "Ubuntu"
    else:
        return "Another System"