#百度提交数据
import requests
kv={'wd':'python'}
r=requests.get("https://www.baidu.com",params=kv)
r.encoding='utf-8'
print(r.status_code)
print(r.request.headers)
print(r.url)
print(len(r.text))
