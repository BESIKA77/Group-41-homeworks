def calculate_best_student(grades):
    best_student = ""
    best_average = 0

    for student, marks in grades.items():
        average = sum(marks) / len(marks)
        print(f"{student}-ის საშუალო ნიშანი: {average}")

        if average > best_average:
            best_average = average
            best_student = student

    return best_student, best_average

# მაგალითი მონაცემები:
student_grades = {
    "ანა": [85, 90, 78],
    "გიორგი": [92, 88, 84],
    "ნინო": [89, 91, 80]
}

best_student, best_average = calculate_best_student(student_grades)
print(f"საუკეთესო სტუდენტია {best_student} საშუალო ნიშანი: {best_average}")




def calculate_stats(grades):
    max_grade = max(grades)
    min_grade = min(grades)
    avg_grade = sum(grades) / len(grades) if len(grades) > 0 else 0
    return max_grade, min_grade, avg_grade

# მაგალითი:
grades = [75, 80, 92, 88, 61]
max_grade, min_grade, avg_grade = calculate_stats(grades)
print(f"მაქსიმალური: {max_grade}, მინიმალური: {min_grade}, საშუალო: {avg_grade}")






def filter_grades(grades):
    filtered_grades = [grade for grade in grades if grade > 50]
    return filtered_grades

# მაგალითი:
grades = [45, 67, 80, 35, 90, 56]
filtered_grades = filter_grades(grades)
print(f"50-ზე მეტი ქულები: {filtered_grades}")






def reverse_numbers(numbers):
    return numbers[::-1]

# მაგალითი:
numbers = [10, 20, 30, 40, 50]
reversed_numbers = reverse_numbers(numbers)
print(f"შებრუნებული სია: {reversed_numbers}")










def calculate_average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0

# მაგალითი:
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(f"საშუალო მნიშვნელობა: {average}")
