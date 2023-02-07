while True:
    try:
        num1 = int(input("Enter number n: "))
        if num1 <= 0:
            raise Exception
        
        break
    except ValueError:
        print("Wrong user input! Integer needed.")
    except Exception:
        print("Number n must be positive!")
        
print(f"Number n is: {num1}")

while True:
    try:
        num2 = int(input("Enter number k: "))
        
        break
    except ValueError:
        print("Wrong user input! Integer needed.")
        
print(f"Number k is: {num2}")
      
all_nums = []  
for _ in range(num1):
    while True:
        try:
            num3 = int(input("Enter number x: "))
            all_nums.append(num3)
            
            break
        except ValueError:
            print("Wrong user input! Integer needed.")
            
print(f"All numbers are: {all_nums}")

#And so on...