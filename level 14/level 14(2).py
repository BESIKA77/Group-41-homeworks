# Number 1 - ვანგარიშობთ 1 დან 10 მდე რიცხვების ჯამს
sum_numbers = 0


for num in range(1, 11):
    sum_numbers += num


print("The sum of numbers from 1 to 10 is:", sum_numbers)


# Number 2 - რიცხვების კვადრატები
for num in range(1, 16):
    square = num ** 2
    print(f"The square of {num} is: {square}")

# Number 3 - რიცხვების კვადრატების ჯამი 1 დან 5 ის ჩთვლით
sum_squares = 0


for num in range(1, 6):
    square = num ** 2
    sum_squares += square


print("The sum of squares of numbers from 1 to 5 is:", sum_squares)


# Number 4 - რიცხვები რომლებიც იყოფა 3 ზე და 5 ზე 100 მდე

for num in range(1, 101):
    
    if num % 3 == 0 and num % 5 == 0:
        print(num)

# Number 5 - 1 დან 10 ის ჩათვლით უკუღმა

for num in range(10, 0, -1):
    print(num)

#------------------------------------------------------------------#
# While loop 
# -----------------------------------------------------------------#
# Number 1 - რიცხვების ჯამი

num = input("Enter a number: ")

sum_digits = 0

index = 0

while index < len(num):
    
    digit = num[index]
    
    if digit.isdigit():
        
        sum_digits += int(digit)
    
    index += 1

print("Sum of digits:", sum_digits)


# Number 2 - 10 დან 1 მდე

num = 10 
while num > 0:
    print(num)
    num = num - 1


# Number 3 - ყველა მთელი რიცხვის ჯამი 1 დან 100 მდე
num = 1
sum_numbers = 0

while num <= 100:
    sum_numbers += num
    num += 1

print("The sum of all integers from 1 to 100 is:", sum_numbers)


# Number 4 - 
num = 1

while num <= 10:
    square = num * num
    print("The square of", num, "is", square)
    num += 1

#-----------------------------------------------------------#
# if-else
#-----------------------------------------------------------#
# Number 1 - 
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Number 2 - 



# Number 3 - დადებითი,უარყოფითი,ნული
Num = int(input("please enter number: "))

if Num > 0:
    print("your number is positive")
elif Num == 0:
    print("you entered zero(0)")
else:
    print("your number is negative")


# Number 4 - 
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

if height < 1.5:
    print("Short stature")
elif height < 1.8:
    print("Average height")
else:
    print("Tall stature")






