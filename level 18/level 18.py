# append()
# homework 18-N1
# მაგალითი 1
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

# მაგალითი 2
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')
print(fruits)

# მაგალითი 3
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)
print(list1)

# მაგალითი 4
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)

# მაგალითი 5
numbers = [1, 2, 3]
new_tuple = (4, 5)
numbers.append(new_tuple)
print(numbers)


# clear()
# მაგალითი 1
numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers) 

# მაგალითი 2
fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits) 

# მაგალითი 3
nested_list = [[1, 2], [3, 4], [5, 6]]
nested_list.clear()
print(nested_list)  

# მაგალითი 4
options = ['yes', 'no', 'maybe']
options.clear()
print(options) 

# მაგალითი 5
data = [1, 'apple', (3, 4), {'a': 5}]
data.clear()
print(data)  


# copy()
# მაგალითი 1
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print(copied_list) 

# მაგალითი 2
original_list = ['apple', 'banana', 'cherry']
copied_list = original_list.copy()
print(copied_list) 

# მაგალითი 3
original_nested_list = [[1, 2], [3, 4], [5, 6]]
copied_nested_list = original_nested_list.copy()
print(copied_nested_list) 

# მაგალითი 4
original_list = [1, 2, 3]
copied_list = original_list.copy()
original_list.append(4)
print(original_list)
print(copied_list)   

# მაგალითი 5
original_list = [1, 'apple', (3, 4), {'a': 5}]
copied_list = original_list.copy()
print(copied_list) 


# count()
# მაგალითი 1
numbers = [1, 2, 3, 4, 2, 2, 5]
count_of_twos = numbers.count(2)
print("Count of twos:", count_of_twos)

# მაგალითი 2
words = ['apple', 'banana', 'apple', 'cherry', 'banana']
count_of_apples = words.count('apple')
print("Count of apples:", count_of_apples)

# მაგალითი 3
nested_list = [[1, 2], [3, 4], [1, 2]]
count_of_sublist = nested_list.count([1, 2])
print("Count of sublist [1, 2]:", count_of_sublist)

# მაგალითი 4
pairs = [(1, 2), (3, 4), (1, 2), (5, 6)]
count_of_pairs = pairs.count((1, 2))
print("Count of pair (1, 2):", count_of_pairs)  

# მაგალითი 5
data = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}]
count_of_alice = data.count({'name': 'Alice', 'age': 30})
print("Count of {'name': 'Alice', 'age': 30}:", count_of_alice)


# extend()
# მაგალითი 1
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  

# მაგალითი 2
fruits = ['apple', 'banana']
additional_fruits = ['cherry', 'date']
fruits.extend(additional_fruits)
print(fruits) 

# მაგალითი 3
list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
list1.extend(tuple1)
print(list1) 

# მაგალითი 4
list1 = ['a', 'b']
string1 = 'cd'
list1.extend(string1)
print(list1)

# მაგალითი 5
list1 = [1, 2, 3]
generator = (x ** 2 for x in range(3))
list1.extend(generator)
print(list1) 


# index()
# მაგალითი 1
numbers = [10, 20, 30, 20, 40, 50]
index = numbers.index(20)
print("Index of 20:", index) 

# მაგალითი 2
fruits = ['apple', 'banana', 'cherry', 'banana']
index = fruits.index('banana')
print("Index of 'banana':", index)

# მაგალითი 3
nested_list = [[1, 2], [3, 4], [5, 6]]
index = nested_list.index([3, 4])
print("Index of [3, 4]:", index) 

# მაგალითი 4
numbers = [10, 20, 30, 20, 40, 50]
index = numbers.index(20, 2)  # Search for 20 starting from index 2
print("Index of 20 after index 2:", index) 

# მაგალითი 5
numbers = [10, 20, 30, 40, 50]
try:
    index = numbers.index(60)
    print("Index of 60:", index)
except ValueError:
    print("Element not found in the list")