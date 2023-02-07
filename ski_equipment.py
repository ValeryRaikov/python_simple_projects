class SkiEquipment:
    def __init__(self, ski_brand, ski_model, ski_year, ski_price):
        self.ski_brand = ski_brand
        self.ski_model = ski_model
        self.ski_year = ski_year
        self.ski_price = ski_price
        
    def __str__(self):
        return f"Ski brand/model {self.ski_brand} {self.ski_model} from {self.ski_year} year cost {self.ski_price} leva."
    
skis = [
    SkiEquipment("Atomic", "Redster", 2021, 799),
    SkiEquipment("Nordica", "Dobermann", 2020, 699),
    SkiEquipment("Rossignol", "Hero", 2020, 599),
    SkiEquipment("Salomon", "Race SI", 2022, 699),
    SkiEquipment("Völkl", "Racetiger", 2021, 699)
]

def sort_ski_name(skis):
    sorted_ski_name = sorted(skis, key=lambda x: x.ski_brand, reverse = False)
    for i in sorted_ski_name:
        print(i)
    
def sort_ski_year(skis):
    sorted_ski_year = sorted(skis, key=lambda x: x.ski_year, reverse = False)
    for i in sorted_ski_year:
        print(i)
    
def sort_ski_price(skis):
    sorted_ski_price = sorted(skis, key=lambda x: x.ski_price, reverse = False)
    for i in sorted_ski_price:
        print(i)
    
sort_ski_name(skis)
print()
sort_ski_year(skis)
print()
sort_ski_price(skis)

def check_for_ski(skis, ski_brand, ski_model):
    for ski in skis:
        if ski.ski_brand == ski_brand and ski.ski_model == ski_model:
            print("Found:", ski)
            return
    print("No such skis in inventory!")
    
def filter_price(skis, ski_price, isFound = False):
    for ski in skis:
        if ski.ski_price == ski_price:
            print("Found:",ski)
            isFound = True
    if isFound == False:        
        print("No such ski price in inventory!")
    
def skis_per_year(skis, ski_year, isFound = False):
    for i in range(len(skis)):
        current_skis = skis[i]
        
        if current_skis.ski_year == ski_year:
            print(f"{current_skis.ski_brand} {current_skis.ski_model}")
            isFound = True
    if isFound == False:        
        print(f"No such skis from {ski_year} year!")
            
check_for_ski(skis, input("Enter ski brand: "), input("Enter ski model: "))
filter_price(skis, int(input("Enter ski price: ")))
skis_per_year(skis, int(input("Enter year: ")))