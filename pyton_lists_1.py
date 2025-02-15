# 1. Python List Transformation

# Problem Statement: You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.

# Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Sort the grades in descending order and display the sorted list.

grades.sort (reverse = True)
print(grades)

# Task 2: Calculate the average grade and display it.

avg = sum(grades)/len(grades)
print(avg)

# Task 3: Replace any grade below 80 with the value Failed.

updated_grades = ["Failed" if grade < 80 else grade for grade in grades]

print (updated_grades)

