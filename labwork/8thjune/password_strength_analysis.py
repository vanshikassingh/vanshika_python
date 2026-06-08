password = input("Enter Password: ")

# Counters
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

digits_list = []
special_list = []

# Special characters set (you can expand if needed)
special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

# Traverse password
for ch in password:
    if ch.isupper():
        upper_count += 1

    elif ch.islower():
        lower_count += 1

    elif ch.isdigit():
        digit_count += 1
        digits_list.append(ch)

    elif ch in special_chars:
        special_count += 1
        special_list.append(ch)

# Strength checking rules
if len(password) < 8:
    strength = "Weak"
else:
    if (upper_count >= 1 and lower_count >= 1 and
        digit_count >= 1 and special_count >= 1):
        strength = "Strong"
    elif (upper_count + lower_count + digit_count + special_count >= 3):
        strength = "Medium"
    else:
        strength = "Weak"

# OUTPUT
print("\nPassword:", password)
print("Uppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)

print("Digits Found:", digits_list)
print("Special Characters Found:", special_list)

print("Password Strength:", strength)
