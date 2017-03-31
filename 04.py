#知乎问题爬取
#1.防爬虫
#2.提交数据
import requests
kv={'user-agent':'Mozilla/5.0'}
url="https://www.zhihu.com/search?=python"
r=requests.get(url,headers=kv)
print(r.request.headers)
print(r.encoding)
print(r.status_code)
r.encoding=r.apparent_encoding
print(len(r.text))
