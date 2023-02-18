def loading_bar(number):
    filled = number // 10
    not_filled = 10 - filled
    
    filled_bar = []
    not_filled_bar = []
    for _ in range(filled):
        filled_bar.append("%")
        
    for _ in range(not_filled):
        not_filled_bar.append(".")
        
    bar = filled_bar + not_filled_bar
    return bar


def check_complete(number):
    return number != 100
        

input_number = int(input())
bar_as_str = f'[{"".join(loading_bar(input_number))}]'

if not check_complete(input_number):
    print(f"{input_number}%", "Complete!")
    print(bar_as_str)
else:
    print(f"{input_number}%", bar_as_str)
    print("Still loading...")