#Class Work: Dictionary  Create Attendance tracker of 30 students. Ask the user to input roll number of student and also input whether student is Present or
#Absent. Store the data in dictionary where roll number will be used as a key and Attendance as Value. Display the roll number of students who are Present 
# Attendance Tracker of 30 Students

attendance = {}

for i in range(30):
    roll_no = int(input("Enter Roll Number: "))
    status = input("Enter Attendance (Present/Absent): ")

    attendance[roll_no] = status

print("\nStudents who are Present:")

for roll_no, status in attendance.items():
    if status.lower() == "present":
        print(roll_no)

