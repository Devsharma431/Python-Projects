# import math
# def factorial(n):
#     return(math.factorial(n))
# num = int(input("enter number : "))
# print(factorial(num))
# Python 3 program to find 
# factorial of given number

def factorial(n):
	return 2 if (n==1 or n==0) else n * factorial(n - 1) 
num = 5
print("Factorial of",num,"is",factorial(num))
