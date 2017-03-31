#亚马逊商品信息的爬取
import requests
url="https://www.zhihu.com/people/hua-deng-deng-87/answers"
try:
    kv={'user-agent':'Mozilla/5.0'}
    r=requests.get(url,headers=kv)
    print(r.status_code)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[2000:10000])
except:
    print("ERROR!")

