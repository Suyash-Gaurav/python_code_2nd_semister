"""
def print_sqr_root(x):      # Defining the function
    if x <= 0:              # logic  to distinguish if x is negative number
        print("Please enter positive numbers only")   # if negative number this line is printed
        return                          # else return the value of x
                                                            # logic for square root, storing the sq root value at result variable
    print("the sq root of", x, "is  ", x ** 0.5)             # printing
print(print_sqr_root(x=int(input("Enter the number: "))))
#print(print_sqr_root(x))           # printing and calling the sq root function and adding the value to x


"""

