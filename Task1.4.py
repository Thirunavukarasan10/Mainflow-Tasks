n_terms = int(input("Enter the number of terms: "))


if n_terms <= 0:
    print("Please enter a positive integer.")
else:
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n_terms):
        print(a, end=" ")
        a, b = b, a + b
