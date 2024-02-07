from datetime import date

class Car:
    
    total = 0
    
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year
        Car.total += 1
        
        
    def car_info(self):
        print(f"The Brand is {self._brand}, Model : {self._model}, Year : {self._year}")
    
    
    def age_of_car(self):
        
        print(date.today().year - self._year)
    
    def total_cars():
        
        print(Car.total)
    
    

class ElectricCar(Car):
    
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        
        
        self._battery_life  = battery_life
        
        
    def battery_info(self):
        
        print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self._battery_life} საათი")
        
        


        
    
car_1 = Car("Bmw","M 5", 2016)
car_2 = Car("Mercedes","E 63", 2017)
car_3 = ElectricCar("Tesla", "Model S", 2022, "5000")

car_1.car_info()
car_1.age_of_car()

car_3.battery_info()

Car.total_cars()