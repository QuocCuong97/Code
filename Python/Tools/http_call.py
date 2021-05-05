import requests

i = 0
while i < 100000:
    x = requests.get('http://localhost:80')
    if (x.status_code == 200):
        print("Request {} successfully!".format(i))
    else:
        print("Request {} failed!".format(i))
    i += 1