n = int(input())
cnt=0
for i in range(n):
    a = int(input())
    if a%2!=0 and a%3==0:
        cnt+=a

print(cnt)