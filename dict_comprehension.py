names = ["Valery", "Filip", "Nikola", "Ivan"]
positions = ["programmer", "dentist", "salesman", "doctor"]

my_dict = {}
for key, value in zip(names, positions):
    my_dict[key] = value
    
print(my_dict)

for i in range(len(names)):
    my_dict[names[i]] = positions[i]
    
print(my_dict)

#Dictionary comprehension!!!
my_dict_comp = {
    key: value for key, value in zip(names, positions)
}

print(my_dict_comp)

my_dict_comp = {
    names[i]: positions[i] for i in range(len(names))
}

print(my_dict_comp)