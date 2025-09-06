# factorial using function and recursion
n=int(input("enter the number "))
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
result=factorial(n)

print("factorial of",n,"is",factorial(n))

