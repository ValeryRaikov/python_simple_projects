class Car:
    def __init__(self, brand, model, fuel_type, fuel_consumption, year, price):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        self.fuel_consumption = fuel_consumption
        self.year = year
        self.price = price
        
    def __str__(self):
        return f"\nVehicle --> {self.brand} {self.model}\nFuel / consumption --> {self.fuel_type} / {self.fuel_consumption}\nYear --> {self.year}\nPrice --> {self.price}"
    
    def __repr__(self):
        return f"\nVehicle --> {self.brand} {self.model}\nFuel / consumption --> {self.fuel_type} / {self.fuel_consumption}\nYear --> {self.year}\nPrice --> {self.price}"
    
cars = [
    Car("Skoda", "Octavia", "diesel", 7.5, 2015, 20000),
    Car("Volkswagen", "Tiguan", "diesel", 8.3, 2018, 35000),
    Car("Audi", "A4", "petrol", 9, 2016, 40000),
    Car("Nissan", "Qashqai", "petrol", 7.3, 2017, 20000)
]

def sort_consumption(cars):
    print(sorted(cars, key = lambda x: x.fuel_consumption, reverse = False))
    
def sort_price(cars):
    print(sorted(cars, key = lambda x: x.price, reverse = False))
    
def check_for_vehicle(cars, brand, model):
    for car in cars:
        if car.brand == brand and car.model == model:
            print(car)
            return
    print("No such vehicle!")
    
def calculate_consumption(cars, brand, model, kilometers):
    for car in cars:
        if car.brand == brand and car.model == model:
            consumption = (car.fuel_consumption * kilometers) / 100
            print(f"Consumption of {car.brand} {car.model} for {kilometers}km is {consumption} liters.")
            return
    print("No such vehicle!")
    
    
sort_consumption(cars)
print()
sort_price(cars)
print()
check_for_vehicle(cars, "Skoda", "Octavia")
calculate_consumption(cars, input("Enter brand: "), input("Enter model: "), float(input("Enter kilometers: ")))