n = int(input())
cnt=0
for i in range(n):
    if n%2!=0 and n%3==0:
        cnt+=1

print(cnt)