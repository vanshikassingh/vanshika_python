total = 0
failed_subjects = 0

for i in range(1, 6):
    marks = int(input(f"Enter marks of Subject {i}: "))
    total += marks

    if marks < 40:
        failed_subjects += 1

percentage = total / 5

if failed_subjects > 0:
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

print("\nTotal Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Number of Subjects Failed:", failed_subjects)
