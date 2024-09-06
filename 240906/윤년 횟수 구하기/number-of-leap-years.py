n= int(input())
yun =0 
nomal=0

for i in range(1, n+1):

    if i%100==0 and i%400!=0:
        nomal+=1

    elif i % 4 ==0:
        yun+=1    
    
    else:
        nomal+=1
    

print(yun)