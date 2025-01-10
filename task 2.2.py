def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10  # Get the last digit
        num //= 10         # Remove the last digit
    return total


number = 12345
print("Sum of digits:", sum_of_digits(number))
