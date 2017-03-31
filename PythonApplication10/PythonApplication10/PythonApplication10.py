'''
def sth(name,type='man'):
    print(name)
    print(type)
sth(name='tom',type='animal')
'''
#8.3 t-shirt
'''
def make_shirt(size,name):
    print(size)
    print(name)
make_shirt('XXL','NIKE')
make_shirt('XXXXXXL','ADIDAS')
make_shirt('S','ARMANI')
'''
#8.5 city
'''
def describe_city(name='dalian',country='china'):
    print(name)
    print(country)
describe_city()
'''
#8.3 return value
'''
def name(first,last):
    full_name=first+last
    return full_name
   
full_name=name('wang','zhengzhi')
print(full_name)
'''
'''
def name(first,last,middle=''):
    if middle:
        full_name=first+middle+last
    else:
        full_name=first+last
    return full_name
full_name=name('wang','zhengzhi')
print(full_name)
full_name=('wang','zheng','zhi')
print(full_name)
'''
def name(first,last):
    persion={'firstname':first,'lastname':last}
    return persion
sth=name('wang','bo')
print(sth)
    






