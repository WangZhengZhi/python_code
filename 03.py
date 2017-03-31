#百度&360搜索提交
#360提交
import requests
kv={'q':'python'}
r=requests.get("https://www.so.com/s?",params=kv)
r.encoding='utf-8'
print(r.request.headers)
print(r.url)
print(len(r.text))
