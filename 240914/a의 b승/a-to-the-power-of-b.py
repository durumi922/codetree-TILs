a,b = map(int,input().split())
pord = 1

for i in range(1,b+1):
    pord *= a

print(pord)