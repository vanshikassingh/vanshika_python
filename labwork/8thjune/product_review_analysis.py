plate = input("Enter Vehicle Number Plate: ")

# 1. Extract parts
state_code = plate[0:2]
district_code = plate[2:4]
series = plate[4:6]
vehicle_number = plate[6:10]

# 2. Count letters and digits
letter_count = 0
digit_count = 0

for ch in plate:
    if ch.isalpha():
        letter_count += 1
    elif ch.isdigit():
        digit_count += 1

# 3. Validation rules
is_valid = True

# Rule 1: first 2 must be alphabets
if not state_code.isalpha():
    is_valid = False

# Rule 2: next 2 must be digits
if not district_code.isdigit():
    is_valid = False

# Rule 3: next 2 must be alphabets
if not series.isalpha():
    is_valid = False

# Rule 4: last 4 must be digits
if not vehicle_number.isdigit():
    is_valid = False

status = "Valid" if is_valid else "Invalid"

# OUTPUT
print("\nVehicle Number:", plate)
print("State Code:", state_code)
print("District Code:", district_code)
print("Series:", series)
print("Vehicle Number:", vehicle_number)

print("\nTotal Letters:", letter_count)
print("Total Digits:", digit_count)

print("\nVehicle Number Status:", status)
