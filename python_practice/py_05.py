n = eval(input())
x=0
for i in range(1,n+1):
    x=x+i
for i in range(1,n):
    print(i,"+",sep="",end="")
print(n,"=",x)
