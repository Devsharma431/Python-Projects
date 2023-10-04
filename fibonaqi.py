# def fibonaqi(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonaqi(n-1) + fibonaqi(n-2)
# n = int(input("enter a no. :"))
# print(fibonaqi(n))
n = 1000000
num1 = 0
num2 = 1
next_number = num2
count = 1

while count <= n:
	print(next_number, end=" ")
	count += 1
	num1, num2 = num2, next_number
	next_number = num1 + num2
print()
