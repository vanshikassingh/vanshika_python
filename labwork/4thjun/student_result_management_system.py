total = 0
failed = 0

for i in range(1, 6):
    marks = int(input(f"Enter marks of Subject {i}: "))
    total += marks

    if marks < 40:
        failed += 1

percentage = total / 5

if failed > 0:
    grade = "Fail"
elif percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Failed Subjects:", failed)
