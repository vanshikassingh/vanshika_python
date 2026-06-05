marks = [78, 45, 92, 35, 88, 40, 99, 56]

passed_students = []
failed_count = 0
merit_list = []
highest = marks[0]
lowest = marks[0]

for mark in marks:

    if mark >= 40:
        passed_students.append(mark)
    else:
        failed_count += 1

    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

    if mark > 75:
        merit_list.append(mark)

print("Passed Students:", passed_students)
print("Failed Count:", failed_count)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Merit List:", merit_list)
