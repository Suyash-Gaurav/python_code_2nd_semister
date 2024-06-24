P = int(input("Enter principal amount: "))
r = float(input("Enter annual nominal interest rate:  "))
n = int(input("Enter number of times the interest is compounded: "))
t = int(input("Enter number of years: "))

A = P * ((1 + (r / n)) ** (n * t))
print("The annual compound is: ", A)