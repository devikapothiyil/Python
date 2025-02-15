students = []
print("Enter details for 3 students (Name, Subject, Grade):")
for i in range(3):
    # Taking user input and splitting it into parts
    details = input(f"Student {i + 1}: ").split(", ")
    name = details[0]
    subject = details[1]
    grade = int(details[2])  # Convert grade to integer
    students.append((name, subject, grade))

# Print the header
print("+----------------+------------+-------+")
print(f"| {'Name':<14} | {'Subject':<10} | {'Grade':>5} |")
print("+----------------+------------+-------+")

# Print each student's data
for student in students:
    name, subject, grade = student
    print(f"| {name:<14} | {subject:<10} | {grade:>5} |")

# Print the footer
print("+----------------+------------+-------+")
