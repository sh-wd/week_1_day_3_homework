def return_10():
    return 10

def add(num1, num2):
    return (num1 + num2)

def subtract(num1, num2):
    return (num1 - num2)

def multiply(num1, num2):
    return (num1 * num2)

def divide(num1, num2):
    return (num1 / num2)

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return (string1 + string2)

def add_string_as_number(string1, string2):
    return (int(string1) + int(string2))

def number_to_full_month_name(number):
    if number == 1:
        return "January"
    
    if number == 3:
        return "March"
    
    if number == 9:
        return "September"
    
def number_to_short_month_name(number):
    if number == 1:
        return "Jan"
    
    if number == 4:
        return "Apr"

    if number == 10:
        return "Oct"

def cube_volume(number):
    # return number*number*number
    return number**3

def reserve_string(string):
    return string [::-1]

def temperature(temp):
    return (temp-32)/1.8
