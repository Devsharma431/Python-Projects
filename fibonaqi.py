# # FIBONACCI BY FOR LOOP
n = int(input("enter a no : "))
a,b = 0,1
sum = 0
for i in range(0,n):
    print(sum, end= "\n")
    a = b
    b = sum
    sum = a + b
# FIBONACCI BY RECURSION
def rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec(n-1) + rec(n-2)
f = int(input('enter a no :'))
print(rec(f))