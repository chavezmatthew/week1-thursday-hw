# 4. Deep Dive into Python Lists

# Problem Statement: You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]


# Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"

for i in range (len(students)):
    if grades[i] < 80:
        print (students[i], grades[i], activities [i])


# Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]

students_approved = []

for i in range (len(students)):
    if grades[i]>= 80:
        students_approved.append(students[i])


# Task 3: Print the list students_approved

print(students_approved)