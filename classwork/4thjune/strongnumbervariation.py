num = int(input("Enter a number: "))

original = num
sum_fact = 0

while num > 0:
    digit = num % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    sum_fact += factorial
    num //= 10

if sum_fact == original:
    print(original, "is a Strong Number")
else:
    print(original, "is not a Strong Number")
