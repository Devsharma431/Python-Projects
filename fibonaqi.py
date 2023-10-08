# d = int(input("enter ur n. : "))
# a , b = 0,1
# sum =0
# for i in range(0,d):
#     a = b
#     b = sum
#     sum = a+b
#     print(sum, end='')
def fast(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fast(n+1) + fast(n-2)
f = int(input('enter a no : '))
print(fast(f))