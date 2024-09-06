cnt12=0
cnt3=0
cnt2=0
n = int(input())


for i in range(n+1):
    if i==0:
        continue
    elif i%12==0:
        cnt12 += 1
    elif i%6==0:
        cnt3 += 1
    elif i%3==0:
        cnt3 += 1
    elif i%2==0:
        cnt2 += 1
    

print(cnt2,cnt3,cnt12)

# n이 아니라 i로 해야하네
# for i in range(n):