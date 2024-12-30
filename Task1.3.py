def factorial(n):
    result=1
    for i in range(1,1+1):
        result*=i
    return result
number=int(input("enter a number:"))
if number<0:
    print(f"number is denied for negative numbers")
else:
    print(f"the factorial of {number} is {factorial(number)}")        