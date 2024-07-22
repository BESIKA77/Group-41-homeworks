def sum_even_numbers(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum_even_numbers(numbers)) 