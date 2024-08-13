# POP
# homework 16-N1
numbers = [1, 2, 3, 4, 5]

last_element = numbers.pop()
print("Removed element:", last_element)

print("Updated list:", numbers)


# homework 16 -N2
strings = ["apple", "banana", "cherry", "date"]

first_element = strings.pop(0)
print("Removed element:", first_element)

print("Updated list:", strings)


# homework 16-N3
characters = ['a', 'b', 'c', 'd', 'e']

removed_element = characters.pop(2)
print("Removed element:", removed_element)

print("Updated list:", characters)


# homework 16-N4
my_list = [10, 20, 30, 40, 50]

last_element = my_list.pop()
print("Removed element:", last_element)

print("Updated list:", my_list)

# Count
# homework 16-N5
numbers = [1, 5, 2, 5, 8, 5, 3, 5, 5, 9]

count_of_5 = numbers.count(5)

print("Number of times 5 appears:", count_of_5)


# homework 16-N6
strings = ["apple", "banana", "cherry", "date"]
total_count = 0

for s in strings:
    count_in_string = s.count('a')
  
    total_count += count_in_string

print("Total occurrences of 'a':", total_count)


# homework 16-N7
bool_list = [True, False, True, False, True, True, False]

count_true = sum(1 for value in bool_list if value)

print("Number of True values:", count_true)


# homework 16-N8
nested_list = [[1, 2], [3, 4], [3, 4], [5, 6], [3, 4, 5]]

count = 0

for sublist in nested_list:
    
    if sublist == [3, 4]:
        count += 1

print("Occurrences of [3, 4]:", count)


# Len
# homework 16-N9
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

number_of_weekdays = len(weekdays)

print("Number of weekdays:", number_of_weekdays)


# homework 16-N9
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

total_elements = sum(len(sublist) for sublist in nested_list)

print("Nested list:", nested_list)
print("Total number of elements:", total_elements)