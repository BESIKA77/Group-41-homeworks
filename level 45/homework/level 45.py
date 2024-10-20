def count_items(item_list, item):
    count = 0
    for i in item_list:
        if i == item:
            count += 1
    return count




def sum_of_list(num_list):
    total = 0
    for num in num_list:
        total += num
    return total




def average_of_list(num_list):
    total = sum_of_list(num_list)
    count = len(num_list)
    return total / count if count > 0 else 0




def reverse_list(items):
    return items[::-1]
