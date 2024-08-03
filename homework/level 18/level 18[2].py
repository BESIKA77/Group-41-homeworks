# homework 18-1
my_list = [5, 3, 8, 1, 7, 2]

smallest = my_list[0]

for num in my_list[1:]:
    if num < smallest:
        smallest = num 

print(f"The smallest number in the list is: {smallest}") 


# homework 18-2
my_list = [5, 3, 8, 1, 7, 2]

largest = my_list[0]

for num in my_list[1:]:
    if num > largest:
        largest = num  

print(f"The largest number in the list is: {largest}")


# homework 18-3
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

indices = [1, 2, 3, 5]

selected_elements = [my_list[idx] for idx in indices]

for idx, elem in zip(indices, selected_elements):
    print(f"Index {idx} -> Element '{elem}'")


# homework 18-4
integers = [1, 2, 3, 4, 5]
strings = ['a', 'b', 'c', 'd', 'e']

combined = []

min_length = min(len(integers), len(strings))

for i in range(min_length):
    combined.append(strings[i])
    combined.append(integers[i])

if len(integers) > len(strings):
    combined.extend(integers[min_length:])
else:
    combined.extend(strings[min_length:])

print(combined)


# homework 18-5
mixed_list = ['apple', 1, 'banana', 2, 'cherry', 3, 'date', 4]

strings_list = []
integers_list = []

for item in mixed_list:
    if isinstance(item, str):
        strings_list.append(item)
    elif isinstance(item, int):
        integers_list.append(item)

print("Strings List:", strings_list)
print("Integers List:", integers_list)


# homework 18-6
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
list3 = [11, 12, 13, 14, 15]
list4 = [16, 17, 18, 19, 20]

sum_even = 0
sum_odd = 0

for lst in [list1, list2, list3, list4]:
    for num in lst:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}")


# homework 18-7
list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10, 11, 12]
list3 = [13, 14, 15, 16, 17, 18]
list4 = [19, 20, 21, 22, 23, 24]

even_numbers = []
odd_numbers = []

for lst in [list1, list2, list3, list4]:
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)


# homework 18-8
original_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

lengths_list = [len(item) for item in original_list]

print("Original List:", original_list)
print("Lengths List:", lengths_list)


# homework 18-9
list1 = ['apple', 1, 'banana', 2, 'cherry', 3]
list2 = [4, 'date', 'elderberry', 5, 6]
list3 = ['fig', 7, 8, 'grape']

integers_list = []
strings_concatenated = ''

for lst in [list1, list2, list3]:
    for item in lst:
        if isinstance(item, int):
            integers_list.append(item)
        elif isinstance(item, str):
            strings_concatenated += item

print("Integers List:", integers_list)
print("Concatenated Strings:", strings_concatenated)


# # homework 18-10
original_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

even_index_elements = original_list[::2]

print("Elements from even indices:", even_index_elements)