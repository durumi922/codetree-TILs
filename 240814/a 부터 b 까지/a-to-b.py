a,b = map(int,input().split())

print(a,end=" ")
while a < b:
    if a%2!=0:
        a= a*2
        print(a,end=" ")
    elif a%2==0:
        a= a+3
        print(a,end=" ")