a,b = map(int,input().split())

print(a,end=" ")
while a < b:
    if a%2!=0:
        a= a*2

        if a>b:
            break

        print(a,end=" ")

    elif a%2==0:
        a= a+3

        if a>b:
            break   

        print(a,end=" ")