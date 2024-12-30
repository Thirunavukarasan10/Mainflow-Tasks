number = int(input("Enter a number: "))
num_digits = len(str(number))
sum_of_powers = sum(int(digit) ** num_digits for digit in str(number))
if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
