def validate_length(password):
    return 6 <= len(password) <= 10


def validate_letters_digits(password):
     return password.isalnum()


def validate_at_least_two_digits(password):
    counter_digits = 0
    for char in password:
        if char.isdigit():
            counter_digits += 1
            
    return counter_digits >= 2


def final_validation(password):
    errors = []
    if not validate_length(password):
        errors.append("Password must be between 6 and 10 characters")
    if not validate_letters_digits(password):
        errors.append("Password must consist only of letters and digits")
    if not validate_at_least_two_digits(password):
        errors.append("Password must have at least 2 digits")
        
    return errors
        

input_password = input()

ers = final_validation(input_password)

if len(ers):
    for er in ers:
        print(er)
else:
    print("Password is valid")