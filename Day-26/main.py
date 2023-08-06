# # List comprehension  *
# numbers = [1, 2, 3]
# new_numbers = [n+1 for n in numbers]
# print(new_numbers)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_list2 = [n * 2 for n in range(1,5)]
# print(new_list2)


# # Conditional List Comprehension
# names = ['Alex', "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)

# # Challenge 26.1
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [num * num for num in numbers]
# print(squared_numbers)


# # Challenge 26.2
# result = [num for num in numbers if num % 2 == 0]
# print(result)

# # Challenge 26.3 (Harder)
# f1 = open("file1.txt", "r")
# f2 = open("file2.txt", "r")
# f1_list = f1.readlines()
# f2_list = f2.readlines()

# result = [int(num) for num in f1_list if num in f2_list]
# print(result)

# # Udemy 26.3 implementation
# with open("file1.txt") as file1:
#     f1_data = file1.readlines()
# with open("file2.txt") as file2:
#     f2_data = file2.readlines()

# then it is my stuff
# go edit the 50 states csv


# Dictionary comprehension
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# import random
# random.seed(42)
# students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
# passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}

# print(passed_students)

# Challenge 26.4
# sentence = "What is the Airspeed Veolcity of an Unladen Swallow?"

# result = {word:len(word) for word in sentence.split()}

# print(result)


# Challenge 26.5
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: ((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}
print(weather_f)
