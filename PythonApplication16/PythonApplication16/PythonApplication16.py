#8.5
'''
def make_pizza(*toppings):
    print(toppings)
make_pizza('apple')
make_pizza('peach','sweet')
'''
'''
def make_pizza(*toppings):
    print("this following is printing")
    for topping in toppings:
        print("-----"+topping)
make_pizza('apple')
make_pizza('banana','peach')
'''
#8.5.1
'''
def make_pizza(size,*toppings):
    print("i will make a "+str(size))
    for topping in toppings:
        print(topping)
make_pizza(12,'apple')
make_pizza(16,'apple',17,'peach')
'''
#8.5.2
'''
def build_info(first,last,**user_info):
    info={}
    info['first_name']=first
    info['last_name']=last
    #info={'first_name':first}
    for key,value in user_info.items():
        info[key]=value
    return info
user=build_info('wang','bo',
                province='henan',
                university='dalian')
print(user)
'''
#8-12
'''
def make_pizza(*toppings):
    for topping in toppings:
        print("the ting is "+topping)
make_pizza('apple')
make_pizza('banana','peach')
'''
'''
def build(first,last,**user_info):
    info={}
    info['first_name']=first
    info['last_name']=last
    for key,value in user_info.items():
        info[key]=value
    return info
print_info=build('wang','zhengzhi',city='dalian',country='china')
print(print_info)
'''
#8-12
'''
def make_pizza(*toppings):
    for topping in toppings:
        print(topping)
make_pizza('apple')
make_pizza('banana')
make_pizza('python')
'''
#8-13
'''
def build_info(first,last,**info):
    user={}
    user['first_name']=first
    user['last_name']=last
    for key,value in info.items():
        user[key]=value
    return user
user_print=build_info('wang','zhengzhi',city='dalian',country='china')
print(user_print)'''
#8-14
'''
def build_car(name,size,**info):
    profile={}
    profile['car_name']=name
    profile['car_size']=size
    for key,value in info.items():
        profile[key]=value
    return profile
car_print=build_car('BMW','big',color='white',modle='5')
print(car_print)
'''





    


