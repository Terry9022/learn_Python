n=eval(input())
for j in range(1,n,2):
    a=int((n-j)/2)
    print(" "*(a)+"*"*j,end='')
    print()
for j in range(n,0,-2):
    a=int((n-j)/2)
    print(" "*(a)+"*"*j,end='')
    print()
