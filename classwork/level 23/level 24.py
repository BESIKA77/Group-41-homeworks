def filter_even_numbers_inplace(numbers):
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 != 0:
            numbers.pop(i) 
        else:
            i += 1 