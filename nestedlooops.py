for i in range(5):
    for j in range(i +1):
        print("&", end=" ")
    print()
for i in range(5):
    for j in range(i-1):
        print('*', end=" ")
    print()
n = 7
for i in range(n + 1):
    print(" " * (n-i) * "*", end=" ")
