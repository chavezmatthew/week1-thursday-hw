# 2. Advanced List Methods and Identity Operators

# Problem Statement:
# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]


# Find out which students both submitted their assignments and attended the class.


submitted_attended = []

for student in submitted:
    if student in attended:
        submitted_attended.append(student)

print (submitted_attended)


# Task 2: Check if the two lists are identical in terms of their content, regardless of order.


submitted.sort()
attended.sort()

identical = submitted == attended
print (identical)


# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

attended_copy = attended [:]
for student in attended_copy:
    if student not in submitted:
        attended.remove (student)

print (attended)