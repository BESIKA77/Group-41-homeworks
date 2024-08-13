# names = ["cotne", "luka", "sandro", "nika", "lasha"]
# print(names[0])
# print(names[2])
# print(names[4])  

# names[3] = "giorgi"
# names[2] = "dachi"
# names[4] = "saba"

# print(names[3])
# print(names[2])
# print(names[4])

names = ["cotne", "luka", "sandro", "nika", "lasha"]
names.append("iakobi")
print(names)

names.pop()
print(names)

cars = ["bmw","mercedes"]
for i in range(5):
    car=input("please enter another car: ")
    
    cars.append(car)
    print(cars)