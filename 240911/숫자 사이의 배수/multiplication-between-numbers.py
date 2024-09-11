a,b = map(int,input().split())
cnt=0
sum1=0
for i in range(a, b+1):
    if i%5==0 or i%7==0:
        cnt += 1
        sum1+=i

if cnt==0:
    print(sum1, sum1)
else:
    print(f"{sum1} {sum1/cnt :.1f}")