#ip地址查询APP
import requests
url="http://www.ip138.com/ips138.asp?ip="
ip=input("IP adress")
r=requests.get(url+str(ip))
if r.status_code==200:
    print("the internet connection is working!")
else:
    print("the internet connection is not working")
r.encoding=r.apparent_encoding
print(r.text[7000:-1500])
