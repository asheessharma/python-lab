n=int(input("enter the number "))

for i in range (1,n+1):
    if i%5==0:
        if i%2==0:
            continue
        else:
            print(i,end=' ')
