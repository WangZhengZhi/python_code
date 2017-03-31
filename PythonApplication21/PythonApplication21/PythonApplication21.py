'''
class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+" is sitting")
    def roll_over(self):
        print(self.name.title()+" is rolled over")
my_dog=Dog('wang',15)
print("my dog s name is"+my_dog.name.title())
print("my dog s age is "+str(my_dog.age))
'''
#9-1
'''
class Restaurant():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def work(self):
        print("the "+self.name.title()+"is working")
    def unwork(self):
        print("the "+self.name.title()+"is not working")
my_restaurant=Restaurant('tom','good')
print("i have a"+my_restaurant.name.title())
my_restaurant.work()
my_restaurant.unwork()
'''
#9-2
'''
class Restaurant():
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def describe(self):
        print(self.name.title()+" is very good")
my_restaurant=Restaurant('tom','high')
print("i have a "+my_restaurant.name)
my_restaurant.describe()
'''
#9-3
'''
class user():
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def describe_user(self):
        print(self.first+" "+self.last)
    def greet_user(self):
        print("welcome !"+self.first+" "+self.last)
my_user=user('wang','zhengzhi')
my_user.describe_user()
my_user.greet_user()
'''
#9.2.1
'''
class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def describe(self):
        full_name=str(self.year)+' '+self.make+' '+self.model
        return full_name.title()
my_car=car('audi','a4','2017')
print(my_car.describe())
'''
#9.2.2
'''
class car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.running=0
    def describe(self):
        full_name= self.make+' '+self.model+' '+str(self.year)
        return full_name.title()
    def read_run(self):
        print(self.make+" had been running "+str(self.running))
my_car=car('audi','a4',2017)
print(my_car.describe())
my_car.read_run()
'''
#9.2.3
'''
class Car():
    def __init__(self,make,modle,year):
        self.make=make
        self.modle=modle
        self.year=year
        self.running=0
    def describe(self):
        print(self.make+' '+self.modle+' '+str(self.year))
    def run(self):
        print("this car had been running "+str(self.running) +"years old")
    def update(self,run_day):
        if run_day>=self.running:
            print("u can not roll back")
        else:
            self.running=run_day
        
my_car=Car('audi','a4',2017)
my_car.describe()
my_car.update(23)
my_car.run()
'''
#9.2.3.3
'''
class Car():

    def __init__(self,make,modle,year):
        self.make=make
        self.modle=modle
        self.year=year
        self.running_mile=0
    def describe(self):
        print(self.make+' '+self.modle+' '+str(self.year)+" years old")
    def update(self,run):
        self.running_mile=run
    def updated(self,runned):
        self.running_mile+=runned
    def had_run(self):
        print("this "+self.make+"had been runed "+str(self.running_mile))
my_car=Car('bmw','525li',2017)
my_car.describe()
my_car.update(1000)
my_car.updated(2000)
my_car.had_run()
'''
#9-4
'''
class Restaurant():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        self.number=0
    def work(self):
        print("the "+self.name.title()+"is working")
    def unwork(self):
        print("the "+self.name.title()+"is not working")
    
    def number_served(self,numbers):
        self.number+=numbers
        print("this restaurant had "+str(self.number)+" people eat there")


my_restaurant=Restaurant('tom','good')
print("i have a"+my_restaurant.name.title())
my_restaurant.work()
my_restaurant.unwork()
my_restaurant.number_served(23)
'''
#9-5







       
        




        


        
       
