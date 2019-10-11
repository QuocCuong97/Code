import re
op = open("/etc/os-release", "rt")
re_1 = op.read()
sear_1 = re.search("CentOS", re_1)
sear_2 = re.search("Ubuntu", re_1)
if (sear_1):
    print("He Dieu Hanh: CentOS")
elif (sear_2):
    print("He Dieu Hanh: Ubuntu")
else:
    print("Another System")