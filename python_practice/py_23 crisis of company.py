n=eval(input())
N=input().split(" ")
k=eval(input())
K=input().split(" ")
c=0
t=-1
s=0
C=N.copy()
for i in range(len(N)):
    N[i]=eval(N[i])
    C[i]=eval(C[i])
for i in range(len(K)):
    K[i]=eval(K[i])
    if not 1<=K[i]<=n:
        K.remove(K[i])
    if K.count(K[i])>1:
        K.remove(K[i])
    
for i in range(len(K)):
    K[i]=K[i]-1
K.sort()
for i in range(len(K)):
    a=K[i]
    b=N[a]
    N.remove(b)
    N.insert(0,0)
for i in range(len(N)):
    c=c+N[i]
    if N[i]>t:
        t=N[i]
        
    
s=C.index(t)+1

print(c)
print(s,t)


