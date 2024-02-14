class Car:
    
     
    def __new__(cls, *args, **kwargs):
         
        instance = super().__new__(cls)
   
   
        return instance

    
    def __init__(self, brand, model, year) -> None:
     
     self._brand =  brand
     self._model = model
     self._year = year
         
         
    @property
    def brand(self):
        
        return self._brand
        
    @property
    def model(self):
        
        return self._model
    
    @property
    def year(self):
        
        return self._year
    
    
    @brand.setter
    def brand(self, value):
        
        if isinstance(value, str) and value.isalpha():
            self._brand = value
        else:
            raise ValueError("Brand Name must be STR")
      
        
    @model.setter
    def model(self, value):
        if isinstance(value, str) and value.isalpha():
            self._model = value
        else:
            raise ValueError("Model Name must be STR")
        
    @year.setter
    def year(self, value):
        
        if isinstance(value, int):
            self._year = value
            
        else:
            raise ValueError("Year Must be Number")
        
        
        
        


car1 = Car("Mercedes", "C class", 2020)


print(car1.year, car1.brand, car1.model)

car1.year = 2024


print(car1.year, car1.brand, car1.model)

try : 
    
    car1.year = "2024"
    
except:
    
    print("Value Error")