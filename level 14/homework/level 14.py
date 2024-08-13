# For Loop
# --------------------------------------------------#
#  გამოგვაქვს ყველა ინტეჯერი 0 დან 20 ის ჩათვლით
for i in range(20):
    print(12)

# გამოგვაქვს 10 ნატურალური რიცხვი
for i in range(10):
    print(i)


# გამოგვაქვს ლუწი რიცხვები
for i in range(0, 101, 2):
    print(i)

# გამოგვაქვს კენტი რიცხვები
for i in range(1, 101, 2):
    print(i)

# Number 4
num = int(input("Enter a number: "))

sum = 0
for i in range(1, num + 1):
    sum += i
print(sum)

# გამოგვაქვს 5-ის ჯერადი რიცხვები
for i in range(5, 55, 5):
    print(i)
#----------------------------------------#
# While Loop
# ---------------------------------------#
# Number 1 - გამოგვაქვს რიცხვები 0 დან 20 ის ჩათვლით
num = 0
while num < 21:
    print(num)
    num = num + 1

# Number 2 - ვანგარიშობთ 1 დან 10 მდე რიცხვების ჯამს
num = 1
sum = 0

while num <= 10:
    sum += num
    num += 1

print("The sum of numbers from 1 to 10 is:", sum)


# Number 3 - გამოცნობანა

correct_number = 7

guess = int(input("Guess a number between 1 and 10: "))

while guess != correct_number:
    print("Wrong guess. Try again!")
    guess = int(input("Guess a number between 1 and 10: "))


print("Congratulations! You guessed the correct number:", correct_number)

# Number 4 - სიის ინდექსების გაორმაგება
numbers = [1, 2, 3, 4, 5]

index = 0
new_numbers = []

while index < len(numbers):
    doubled_number = numbers[index] * 2
    new_numbers.append(doubled_number)
    index += 1

print("Original list:", numbers)
print("Doubled list:", new_numbers)

# Number 5 - სწორი პასუხის გაგება
correct_answer = "password123"
name = input("enter your name ")

guess = input("please enter your password: ")

while guess != correct_answer:
    print("it's incorrect,please try again!")
    guess = input("please enter your password: ")
print("password is correct!welcome back", name + "!")
# ---------------------------------------------------------#
# if - else
# ---------------------------------------------------------#
# Number 1 - დილა - შუადღე
hour = int(input('enter what hour is now: '))
if hour < 12:
    print("good morning!")
else:
    print("good afternoon!")

# Number 2 - ლუწი თუ კენტი
number = int(input("please enter number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Number 3 - ცხელა თუ არა
temperature = int(input('enter temperature: '))
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot!")

# Number 4 - ხარ თუ არა მოზარდი
age = int(input('please enter your age: '))
if age >13 and age <18:
    print('You are not a teenager!')
else:
    print('You are a teenager!')








    


