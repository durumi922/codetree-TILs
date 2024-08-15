n = int(input())
a = n 

for i in range(n):
    for j in range(n):
        print(f"({a},{n-j})", end=" ")
    a = a - 1
    print()