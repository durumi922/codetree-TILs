n = int(input())

for i in range(1, n+1):
    t1=0 #왜지..........
    if i%3==0:
        print(0,end=" ")
    else:
        for t in str(i): 
            if t=='3' or t=='6' or t=='9' :
                t1 = 1
        if t1: 
            print(0,end=' ')
        else: print(i,end=' ')