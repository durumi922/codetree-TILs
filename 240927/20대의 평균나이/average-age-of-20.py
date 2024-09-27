sum_p = 0
cnt = 0
while True:
    p = int(input())

    if p >= 30 or p < 20:
        break

    sum_p += p
    cnt +=1


print(f"{sum_p/cnt:.2f}")


#20대 외에 10대에 대해 고려가 안되어있음