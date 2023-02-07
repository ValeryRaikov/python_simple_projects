class Cellphone:
    def __init__(self, phone_brand, phone_model, free_space, year, price, rating):
        self.phone_brand = phone_brand
        self.phone_model = phone_model
        self.free_space = free_space
        self.year = year
        self.price = price
        self.rating = rating
        
    def __repr__(self):
        return f"Cellphone --> {self.phone_brand} {self.phone_model}, {self.free_space} GB, {self.year} year, {self.price} leva, {self.rating}/10 stars"
    
cellphones = [
    Cellphone("Samsung", "S22", 256, 2022, 1499, 8.4), 
    Cellphone("Samsung", "Z-Flip", 512, 2023, 2799, 9.1), 
    Cellphone("Huawei", "Nova 30", 128, 2021, 999, 7.7), 
    Cellphone("Iphone", "13Pro", 512, 2022, 2399, 9.3)
]

def add_cellphone():
    new_phone_brand = input("Enter phone brand: ")
    new_phone_model = input("Enter phone model: ")
    new_free_space = int(input("Enter free space: "))
    new_year = int(input("Enter year: "))
    new_price = float(input("Enter price: "))
    new_rating = float(input("Enter rating: "))
    
    new_cellphone = Cellphone(new_phone_brand, new_phone_model, new_free_space, new_year, new_price, new_rating)
    cellphones.append(new_cellphone)
    
    print(f"You added: {new_cellphone} to the list of cellphones")
    print(cellphones)
    
def sort_by_price(cellphones):
    sorted_cellphones_price = sorted(cellphones, key = lambda x: x.price)

    for cellphone in sorted_cellphones_price:
        print(f"For {cellphone.phone_brand} {cellphone.phone_model} the price is: {cellphone.price} leva")
    
def sort_by_rating(cellphones):
    sorted_cellphones_rating = sorted(cellphones, key = lambda x: x.rating)
    with open("Cellphone_catalog.txt", "w") as wf:
        for cellphone in sorted_cellphones_rating:
            print(f"For {cellphone.phone_brand} {cellphone.phone_model} the rating is: {cellphone.rating}/10 stars")
            
            wf.write(f"{cellphone}\n")
        
def check_phone(cellphones, phone_brand, phone_model):
    isEmpty = True
    for cellphone in cellphones:
        if cellphone.phone_brand == phone_brand and cellphone.phone_model == phone_model:
            print(cellphone)
            isEmpty = False
    if isEmpty:
        print("Could not find phone!")
    
def calculate_delivery(cellphones, add_tax, price_delivery):
    for cellphone in cellphones:
        total_price = (cellphone.price + cellphone.price * add_tax) + price_delivery
        print(f"Total price for {cellphone.phone_brand} {cellphone.phone_model} is: {total_price} leva")
    
add_cellphone()
sort_by_price(cellphones)
sort_by_rating(cellphones)
check_phone(cellphones, phone_brand = input("Enter phone brand: "), phone_model = input("Enter phone model: "))
calculate_delivery(cellphones, add_tax = float(input("Enter additional taxes: ")), price_delivery = float(input("Enter delivery fees: ")))