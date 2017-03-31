#保存一个网页的格式为PDF
import requests
url="https://www.baidu.com"
r=requests.get(url)
print(r.status_code)
path="I:\ myfile.txt"
with open(path,'wb')as f:
    f.write(r.content)
f.close
