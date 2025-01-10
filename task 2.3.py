import math

def calculate_lcm_and_gcd(a, b):
    # Calculate GCD
    gcd = math.gcd(a, b)
  
    lcm = abs(a * b) // gcd
    return lcm, gcd

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))



lcm, gcd = calculate_lcm_and_gcd(num1, num2)

# Display the results
print(f"GCD of {num1} and {num2}: {gcd}")
print(f"LCM of {num1} and {num2}: {lcm}")
