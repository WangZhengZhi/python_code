import requests
url="https://www.baidu.com"
r=requests.get(url)
print(r.status_code)
r.encoding='utf-8'
print(r.text)
