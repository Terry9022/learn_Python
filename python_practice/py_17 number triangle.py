n=eval(input())
a=0
for j in range(1,n+1):
    for i in range(1,j+1):
        a+=1
        print(a,end=" ")
    print()
