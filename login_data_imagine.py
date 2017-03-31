import requests
kv={'suer-agent':'Mozilla/5.0'}
s=requests.session()
login_data={'account':'18941142123','password':'@.@..5211314'}
s.post('https://www.zhihu.com/#signin',login_data)
url=s
r=requests.get(url,headers=kv)
print(r.status_code)
print(s.get('https://www.zhihu.com'))


