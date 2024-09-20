n= int(input())
cnt=0
value=0
for i in range(1, 5001):
    n = n / i
    cnt+=1
    if n <1:
        
        print(cnt)
        break