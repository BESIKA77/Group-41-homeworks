num = 5

# print(True and True) 
# print(True and False) 
# print(False and True) 
# print(False and False) # False 

# print(True or True) # True
# print(True or False) # True
# print(False or True) # True
# print(False or False) # False

print("----------- AND -----------")

print(num >= 1 and num <= 10) # True,რადგან ორივე მოთხოვნა დაკმაყოფილდა(5 მეტია 1-ზე და ნაკლებია 10-ზე)
print(num >= 1 and num <= 4) # False,რადგან and ოპერატორი მკაცრად მოითხოვს ყველა დავალების შესრულებას,აქ კი მხოლოდ ერთი შესრულდა
print(num > 5 and num <= 10) # False,რადგან and ოპერატორი მკაცრად მოითხოვს ყველა დავალების შესრულებას,აქ კი მხოლოდ ერთი შესრულდა
print(num > 5 and num > 10) # False,რადგან and ოპერატორი მკაცრად მოითხოვს ყველა დავალების შესრულებას,აქ კი მხოლოდ ერთი შესრულდა

print("----------- OR -----------")

print(num >= 1 or num <= 10) # True,რადგან or ოპერატორი მოითხოვს რომელიმე დავალების შესრულებას,აქ ორივე დავალება შესრულებულია
print(num >= 1 or num <= 4) # True,რადგან or ოპერატორი მოითხოვს რომელიმე დავალების შესრულებას,აქ პირველი დავალება შესრულდა
print(num > 5 or num <= 10) # True,რადგან or ოპერატორი მოითხოვს რომელიმე დავალების შესრულებას,აქ მეორე დავალება შესრულდა
print(num > 5 or num > 10) # False,რადგან არცერთი არ არის შესრულებული


name="BESO"
surname="gelxauri"
age=14

print(f"my name is {name}.my surname is {surname}.my age is {age}")


print("Your name is {}. Your lastname is {}. my age is {}.".format(name, surname, age))