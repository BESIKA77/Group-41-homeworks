# .Upper() ადიდებს ყველა ასოს
# შევქმნათ ცვლადი პატარა ასოებით
txt = "Hello my friends" 

# x-ში ჩავწერთ ცვლადის სახელს,შემდეგ dot notation და .upper()რაც უკვე გაადიდებს ასოებს
x = txt.upper()

#გამოგვაქვს მნიშვნელობა
print(x)



# .lower() აპატარავებს ყველა ასოს
# შევქმნათ ცვლადი დიდი ასოებით
txt2 = "HELLO WORLD"

# x-ში ჩავწერთ ცვლადის სახელს,შემდეგ dot notation და .lower()რაც უკვე დააპატარავებს ასოებს
x2 = txt2.lower()

#გამოგვაქვს მნიშვნელობა
print(x2)



# .capitalize() პირველ ასოს ტოვებს დიდს,ხოლო დანარჩენ ასოებს აპატარავებს
# შევქმნათ ცვლადი შერეული ასოებით
txt3 = "i'M BeSo gELXAurI"

# x-ში ჩავწერთ ცვლადის სახელს,შემდეგ dot notation და .Capitalize()რაც უკვე გაადიდებს პირველ ასოს და დააპატარავებს ასოებს
x3 = txt3.capitalize()

#გამოგვაქვს მნიშვნელობა
print(x3)


#-------------------------------------------#


# append()
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

# -----------------------------------------------------#

# Pop
# მაგალითი 1
my_list = [1, 2, 3, 4, 5]
last_element = my_list.pop()
print(last_element)
print(my_list)

# მაგალითი 2
my_list = ['a', 'b', 'c', 'd']
element_removed = my_list.pop(2)
print(element_removed) 
print(my_list)

# მაგალითი 3
stack = [10, 20, 30, 40, 50]
popped_value = stack.pop()
print(f"Popped value: {popped_value}, Remaining stack: {stack}")

#_-------------------------------------------------_#

# insert()
# მაგალითი 1
my_list = [1, 2, 3, 4, 5]
my_list.insert(0, 0)
print(my_list)  

# მაგალითი 2
my_list = [1, 2, 4, 5]
my_list.insert(2, 3)
print(my_list)

# მაგალითი 3
my_list = [1, 2, 3, 4]
my_list.insert(len(my_list), 5)
print(my_list)