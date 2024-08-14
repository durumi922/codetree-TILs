n = int(input())

for i in range(n, 101):

    if n >= 90:
        print("A",end=" ")


    elif 89 >= n >= 80:
        print("B",end=" ")

    
    elif 79 >= n >= 70:
        print("C",end=" ")


    elif 69 >= n >= 60:
        print("D",end=" ")

    elif n <= 60:
        print("F",end=" ")

    n= n+1