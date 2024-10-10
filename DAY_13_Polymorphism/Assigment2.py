class Car:
    def __init__(self,brand,model,distance):
        self.brand=brand
        self.model=model
        self.distance=distance
class Electric_car(Car):
    def calulate_milage(self,power):
        milage=self.distance/power
        print(milage)
class Fuel_car(Car):
    def calulate_milage(self,fuel_consume):
        milage=self.distance/fuel_consume
        print(milage)
    
print("The Milage of Toyato S3")
brandobj=Electric_car("toyata","S3",200)
brandobj.calulate_milage(20)
print("The Milage of Mahindra Scorpio")
brandobj1=Fuel_car("Mahindra","Scorpio",5000)
brandobj1.calulate_milage(100)



        
        
        