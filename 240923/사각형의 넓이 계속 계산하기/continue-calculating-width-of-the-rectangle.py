while True:
    w,h,s = map(str,input().split())
    w=int(w)
    h=int(h)

    print(w*h)

    if s == "C":
        break