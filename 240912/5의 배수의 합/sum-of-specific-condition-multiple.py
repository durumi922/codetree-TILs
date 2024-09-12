#a, b 공백 구분해서 입력받기
a,b = map(int,input().split())
result = 0

if b>a:                          #a,b의 대소관계가 보장되지 않으므로 b가 큰 경우
    for i in range(a, b+1):
        if i % 5 == 0:           #5의 배수인 경우 result에 값을 더함
            result += i

else:                             #a가 큰 경우
    for i in range(b, a+1):
        if i % 5 == 0:
            result += i


print(result)