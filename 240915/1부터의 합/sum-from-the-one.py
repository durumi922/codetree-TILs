n = int(input())
hap=0
num=0


for i in range(1,101,1):
    
    hap += i        
    if hap > n:     #n을 넘는 순간
        num = i     #더해진 숫자 값을 저장함
        break

print(num)