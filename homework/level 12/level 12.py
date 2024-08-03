for i in range(10):
    print(i)



for i in range(20):
    print("me miyxavrs awaruli awapuri")

# ------------------------------------------#
age=1
while age<5:
    print(age)
    age=age+1


word=0
while word<3:
    print("Hello")
    word=word+1

# -------------------------------------------#
age=int(input("please enter your age: "))
if age >= 18:
    print("leggal to buy ciggarete")
else:
    ("ileggal to buy ciggarete")


number=int(input("please enter number: "))
if number == 10:
    print("correct!")
else:
    print("incorrect!")
#---------------------------------------------#
age=int(input("please enter your age"))
if age <= 10:
    print("child")
elif age <18 and age > 10:
    print("teenager")
else:
    print("Adult")
#----------------------------------------------#
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("The triangle can be constructed.")
else:
    print("The triangle can't be constructed.")