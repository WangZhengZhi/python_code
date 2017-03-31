import requests
url="https://www.baidu.com"
r=requests.get(url)
if r.status_code:
    print("internet is okay!")
else:
    print("iinternet is not okay")
    r.status_code='utf-8'
print(len(r.text))
print(r.text)
