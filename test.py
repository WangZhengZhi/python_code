class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        #self.run_days=0
    def describe(self):
        print("This car"+self.make+' '+self.model+' '+str(self.year))
class Ecar(Car):
    def _init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=70
    def describe_battery(self):
        print("this car has a "+str(self.battery))
        
my_ecar=Ecar('tesla','s',2017)
my_ecar.describe()
my_ecar.describe_battery()

    



        
     
