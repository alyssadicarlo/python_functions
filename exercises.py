def madlib(name, subject):
    return "%s's favorite subject is %s." % (name, subject)

def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * (9/5)) + 32
    return fahrenheit

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def is_odd(number):
    if is_even(number):
        return False
    if not is_even(number):
        return True

def only_evens(list_of_numbers):
    evens = []
    for number in list_of_numbers:
        if is_even(number):
            evens.append(number)
    return evens

def only_odds(list_of_numbers):
    odds = []
    for number in list_of_numbers:
        if is_odd(number):
            odds.append(number)
    return odds

    
print(madlib("Alyssa", "Math"))
print(celcius_to_fahrenheit(32))
print(fahrenheit_to_celcius(89.6))
print(is_even(2))
print(is_odd(2))
print(only_evens([1,43,64,3,6,7,3,3,6,85,4]))
print(only_odds([1,43,64,3,6,7,3,3,6,85,4]))