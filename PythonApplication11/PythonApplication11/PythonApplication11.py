'''
def sth(first_name,last_name,age=''):
    persion={'first':first_name,'last':last_name}
    if age:
        persion['age']=age
        return age
i=sth('wang','bo',age=27)
print(i)
'''
#8.3.4
'''
def id(first_name,last_name,):
    full_name=first_name.title()+' '+last_name
    return full_name
flag=True
while flag:
    print("please input u name or to enter  'quit'to quit")
    f_name=input("first_name:")
    l_name=input("last_name:")
    if (f_name=='quit')or( l_name=='quit'):
        flag=False
    else:
        id_print=id(f_name,l_name)
        print("\nhello"+id_print)
'''
'''
def id(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()
while True:
    print("\nplease input u name or enter 'quit'to quit")
    f_name=input("please input u first name:")
    if f_name=='quit':
        break
    l_name=input("please input u last name:")
    if l_name=='quit':
        break
    id_print=id(f_name,l_name)
    print("Hello "+id_print)
    '''
#8-6
'''
def city_country(city,country):
    sth=city+','+country
    return sth.title()
while True:
    city_id=input("please input u city or enter 'quit'to quit")
    if city_id=='quit':
        break
    country_id=input("please input u country or enter 'quit'to quit")
    if country_id=='quit':
        break
    id_print=city_country(city_id,country_id)
    print(id_print)
    '''
#8-7
'''
def make_album(name,singer):
    id={'id_name':name,'id_singer':singer}
    return id.title()
    
i=make_album=('adele','hello')
print(i)
'''
'''
def make_album(name,singer):
    id={'id_name':name,'id_singer':singer}
    return id
id_print=make_album('hello','adele')
print(id_print)
'''

