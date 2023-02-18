def is_index_valid(index, elements_count):
    if 0 <= index < elements_count:
        return True
    return False


def check_both_index_valid(index1, index2, elements_count):
    if is_index_valid(index1, elements_count) and is_index_valid(index2, elements_count) and index1 != index2:
        return True
    return False

elements = input().split()
moves = 0

command = input()
while command != "end":
    moves += 1
    index1, index2 = [int(x) for x in command.split()]
    
    if check_both_index_valid(index1, index2, len(elements)):
        if elements[index1] == elements[index2]:
            element = elements[index1]
            elements.pop(index2)
            elements.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        elif elements[index1] != elements[index2]:
            print("Try again!")
    else:
        el_to_add = f"-{moves}a" 
        index_to_add = len(elements) // 2
        for _ in range(2):
            elements.insert(index_to_add, el_to_add)
            
        print("Invalid input! Adding additional elements to the board")
    
    if not elements:
        print(f"You have won in {moves} turns!")
        exit(0)
    
    command = input()
    
print("Sorry you lose :(")
print(*elements, sep = " ")