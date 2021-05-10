def smallest(list_of_numbers):
    smallest = 1e9
    for number in list_of_numbers:
        if number < smallest:
            smallest = number
    return smallest

def largest(list_of_numbers):
    largest = -1e9
    for number in list_of_numbers:
        if number > largest:
            largest = number
    return largest

def shortest(list_of_strings):
    shortest = 1e9
    shortest_string = ""
    for string in list_of_strings:
        if len(string) < shortest:
            shortest_string = string
            shortest = len(string)
    return shortest_string

def longest(list_of_strings):
    longest = 0
    longest_string = ""
    for string in list_of_strings:
        if len(string) > longest:
            longest_string = string
            longest = len(string)
    return longest_string


list_of_numbers = [1,3,6,7,3,6,7,3,2,6]
list_of_strings = ['Alyssa', 'Jessica', 'Gordo']

print(smallest(list_of_numbers))
print(largest(list_of_numbers))
print(shortest(list_of_strings))
print(longest(list_of_strings))
