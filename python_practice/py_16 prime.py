m=eval(input())
for j in range(1,m+1):
    fct=0
    for i in range(1,j+1):
        if j%i==0:
            fct+=1
    if fct ==2:
        print(j,"is prime")
