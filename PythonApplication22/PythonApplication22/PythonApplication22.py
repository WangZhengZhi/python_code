'''
import requests
url="http://www.ip138.com/ips138.asp?ip"
kv=input("please input u ID")
r=requests.get(url,params=kv)
r.encoding='GB2312'
if r.status_code==200:
    print("connection is successful!")
else:
    print("connection ERROR!")
    print("ERROR CODE"+str(r.status_code))
print(r.text[7000:-1600])
flag=True
wd=input("enter 'q' to quit")
while flag:
    if wd=='q':
        break
'''
import requests
url="http://www.ip138.com/ips138.asp?ip"
#url1="http://www.ip138.com:8080/search.asp?mobile="
def seach_id(id):
    #id=idnumber
    
    r=requests.get(url,params=id)
    r.encoding='GB2312'
    if r.status_code==200:
        print("SUCCESSFUL")
        print(r.text[7000:-1600])
    else:
        print("ERROR! ERROR CODE IS"+str(r.status_code))
def seach_tel(tel):
    #tel=telnumber
    url1="http://www.ip138.com:8080/search.asp?mobile="
    url2="&action=mobile"
    url1+=str(tel)+url2
    r=requests.get(url1)
    r.encoding='GB2312'
    if r.status_code==200:
        print("SUCCESSFUL")
        print(r.text[3000:-1200])
    else:
        print("ERROR! ERROR CODE IS"+str(r.status_code))
while True:
    flag=input("u want to seach tel or id?\n enter 'quit'to quit\n")
    if flag=='q':
        break
    else:
        if flag=='tel':
            telnumber=input("enter u tel ")
            seach_tel(telnumber)
        elif flag=='id':
            idnumber=input("enter u id")
            seach_id(idnumber)



    
    









