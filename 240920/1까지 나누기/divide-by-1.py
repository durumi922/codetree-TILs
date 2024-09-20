n= int(input())
cnt=0
l = [1]
for i in l:
    n = n / i
    cnt+=1
    l.append(i + 1)
    if n <1:
        print(cnt)
        break