Python 3.5.3 (v3.5.3:1880cb95a742, Jan 16 2017, 16:02:32) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: C:/Users/apple/Documents/python_code/04.py ============
500
>>> 
============ RESTART: C:/Users/apple/Documents/python_code/04.py ============
500
{'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': 'python-requests/2.13.0', 'Connection': 'keep-alive'}
>>> 
============ RESTART: C:/Users/apple/Documents/python_code/04.py ============
500
{'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'User-Agent': 'python-requests/2.13.0', 'Connection': 'keep-alive'}
>>> 
============ RESTART: C:/Users/apple/Documents/python_code/04.py ============
500
{'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'User-Agent': 'python-requests/2.13.0', 'Connection': 'keep-alive'}
Traceback (most recent call last):
  File "C:/Users/apple/Documents/python_code/04.py", line 11, in <module>
    r=requests.get(headers=kv0)
TypeError: get() missing 1 required positional argument: 'url'
>>> 
============ RESTART: C:/Users/apple/Documents/python_code/04.py ============
python
500
{'Accept': '*/*', 'Connection': 'keep-alive', 'User-Agent': 'python-requests/2.13.0', 'Accept-Encoding': 'gzip, deflate'}
Traceback (most recent call last):
  File "C:/Users/apple/Documents/python_code/04.py", line 12, in <module>
    r=requests.get(url,headers=kv0)
NameError: name 'url' is not defined
>>> 
============ RESTART: C:/Users/apple/Documents/python_code/04.py ============
python
500
{'Connection': 'keep-alive', 'User-Agent': 'python-requests/2.13.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*'}
500
>>> 
============ RESTART: C:/Users/apple/Documents/python_code/04.py ============
Traceback (most recent call last):
  File "C:/Users/apple/Documents/python_code/04.py", line 7, in <module>
    r=requests.get(url,headers=kv)
  File "C:\Users\apple\AppData\Local\Programs\Python\Python35\lib\site-packages\requests\api.py", line 70, in get
    return request('get', url, params=params, **kwargs)
  File "C:\Users\apple\AppData\Local\Programs\Python\Python35\lib\site-packages\requests\api.py", line 56, in request
    return session.request(method=method, url=url, **kwargs)
  File "C:\Users\apple\AppData\Local\Programs\Python\Python35\lib\site-packages\requests\sessions.py", line 474, in request
    prep = self.prepare_request(req)
  File "C:\Users\apple\AppData\Local\Programs\Python\Python35\lib\site-packages\requests\sessions.py", line 407, in prepare_request
    hooks=merge_hooks(request.hooks, self.hooks),
  File "C:\Users\apple\AppData\Local\Programs\Python\Python35\lib\site-packages\requests\models.py", line 303, in prepare
    self.prepare_headers(headers)
  File "C:\Users\apple\AppData\Local\Programs\Python\Python35\lib\site-packages\requests\models.py", line 441, in prepare_headers
    for header in headers.items():
AttributeError: 'set' object has no attribute 'items'
>>> 
============ RESTART: C:/Users/apple/Documents/python_code/04.py ============
{'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'user-agent': 'Mozilla/5.0', 'Connection': 'keep-alive'}
UTF-8
200
8528
>>> #抓取图片
>>> import requests
>>> path="C:/abc.jpg"
>>> url="http://image.nationalgeographic.com.cn/2015/1028/20151028110316191.jpg"
>>> r=requets.get(url)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    r=requets.get(url)
NameError: name 'requets' is not defined
>>> r=requests.get(url)
>>> r.status_code
200
>>> with open(path,'wb')as f:
	f.write(r.content)
	#error

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    with open(path,'wb')as f:
PermissionError: [Errno 13] Permission denied: 'C:/abc.jpg'
>>> 
=============================== RESTART: Shell ===============================
>>> import requests
>>> path="C:/abcd,jpg"
>>> url="http://image.nationalgeographic.com.cn/2015/1028/20151028110316191.jpg"
>>> r=requests.get(url)
>>> r.status_code
200
>>> with open(path,'wb') as f:
	f.write(r.content)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    with open(path,'wb') as f:
PermissionError: [Errno 13] Permission denied: 'C:/abcd,jpg'
>>> 
=============================== RESTART: Shell ===============================
>>> import requests
>>> url="http://image.nationalgeographic.com.cn/2015/1028/20151028110316191.jpg"
>>> path='C:/123.jpg'
>>> r=requests.get(url)
>>> r.status_code
200
>>> with open(path,'wb') as f:
	f.write(r.content)

Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    with open(path,'wb') as f:
PermissionError: [Errno 13] Permission denied: 'C:/123.jpg'
>>> 
