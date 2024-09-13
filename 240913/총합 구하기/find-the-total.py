a, b = map(int,input().split())
sum_1=0

for i in range(a, b+1):
    if i%2==0 and i%3==0 and i%8!=0:
        sum_1 += i


print(sum_1)