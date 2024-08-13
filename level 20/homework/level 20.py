def sum_even_numbers(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(numbers)) 



def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)



def common_elements(list1, list2):
    common_list = []
    for element in list1:
        if element in list2 and element not in common_list:
            common_list.append(element)
    return common_list



def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count



def bubble_sort(lst):
    n = len(lst)

    for i in range(n):

        for index in range(n - i - 1):

            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst



def are_permutations(str1, str2):

    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)



def is_prime(n):
 
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
 
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True



def sort_by_length(strings):
    return sorted(strings, key=len)


