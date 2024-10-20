def word_count(text):
    words = text.split()
    return len(words)




def check_number_sign(num):
    if num > 0:
        return "რიცხვი დადებითია"
    elif num < 0:
        return "რიცხვი უარყოფითია"
    else:
        return "რიცხვი ნულოვანია"




def age_category(age):
    if age < 13:
        return "ბავშვი"
    elif age < 20:
        return "თინეიჯერი"
    elif age < 60:
        return "ზრდასრული"
    else:
        return "ხანდაზმული"




def separate_even_odd(num_list):
    even_numbers = []
    odd_numbers = []
    for num in num_list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers, odd_numbers





def find_average(num_list):
    total = sum(num_list)
    count = len(num_list)
    return total / count if count > 0 else 0
