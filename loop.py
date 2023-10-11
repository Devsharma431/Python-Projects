# count = 0
# while( count < 8):
#     count = count + 1
#     print("Hello worldS")
# n = int(input("enter a no : "))
# # 1 to 100 program
# for i in range(0, n):
#     print(i, end= "\n")
#  100 to  1 program
# print("-----------------------------------------------")
# for i in range(n,0,-1):
#     print(i, end= "\n")
# # 
# sum_of_natural_numbers = 0
# for i in range(1, n):
#     sum_of_natural_numbers += i
# print("The sum of the first 10 natural numbers is:", sum_of_natural_numbers)
import math 
def s(n):
    return math.factorial(n)
j = int(input("enter a no : "))
print(s(j))
f = 0
for i in range(0, j):
    f = j * 1
    f -=  1
    print(f, end= "\n")