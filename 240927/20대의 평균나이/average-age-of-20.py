sum_p = 0
cnt = 0
while True:
    p = int(input())

    if p >= 30:
        break

    sum_p += p
    cnt +=1


print(f"{sum_p/cnt:.2f}")