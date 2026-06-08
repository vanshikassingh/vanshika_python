emp_id = input("Enter Employee ID: ")

# 1. Count uppercase letters
upper_count = 0
for ch in emp_id:
    if ch.isupper():
        upper_count += 1

# 2. Count digits
digit_count = 0
digits_list = []
for ch in emp_id:
    if ch.isdigit():
        digit_count += 1
        digits_list.append(int(ch))

# 3. Extract joining year (EMP + 4 digits after it)
joining_year = emp_id[3:7]

# 4. Extract employee name (after year till last 3 digits)
employee_name = emp_id[7:-3]

# 5. Validation rules
is_valid = True

# Rule 1: starts with EMP
if not emp_id.startswith("EMP"):
    is_valid = False

# Rule 2: year must be 4 digits
if not joining_year.isdigit() or len(joining_year) != 4:
    is_valid = False

# Rule 3: last 3 characters must be digits
if not emp_id[-3:].isdigit():
    is_valid = False

# 7. Sum of digits
digit_sum = sum(digits_list)

# 8. Final status
status = "Valid" if is_valid else "Invalid"

# OUTPUT
print("\nEmployee ID:", emp_id)
print("Uppercase Letters:", upper_count)
print("Digits:", digit_count)
print("Joining Year:", joining_year)
print("Employee Name:", employee_name)
print("Digit List:", digits_list)
print("Sum of Digits:", digit_sum)
print("ID Status:", status)
