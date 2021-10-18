n=input().split()
for i in range(len(n)):
    n[i]=eval(n[i])
N=n[0]
M=n[1]
y=(M-N*2)/2
x=(N*4-M)/2
if x%1==0 and x>=0 and y%1==0 and y>=0:
    print("YES")
    print(int(x),int(y))
else:
    print("NO")
