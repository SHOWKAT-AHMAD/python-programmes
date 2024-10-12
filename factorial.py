x=int(input("enter a number: "))
def factorial(x):
    if x == 0:
        return 1
    return factorial(x-1)*x
print("the factorial of number is: ",factorial(x))
