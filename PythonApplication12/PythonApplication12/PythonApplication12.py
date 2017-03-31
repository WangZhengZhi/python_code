import requests
while True:
    url="http://isscp.dlu.edu.cn"
    r=requests.get(url)
    if r.status_code==200:
        print("successful!!!!!")
    else:
        break
    print(r.text)