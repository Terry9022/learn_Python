lst=[]
n=input().split()
for i in range(len(n)):
    n[i]=eval(n[i])
m=input().split()
for i in range(len(n)):
    m[i]=eval(m[i])
h=input().split()
for i in range(len(n)):
    h[i]=eval(h[i])
lst.append(n)
lst.append(m)
lst.append(h)
ls=[]
n1=input().split()
for i in range(len(n)):
    n1[i]=eval(n1[i])
m1=input().split()
for i in range(len(n)):
    m1[i]=eval(m1[i])
h1=input().split()
for i in range(len(n)):
    h1[i]=eval(h1[i])
ls.append(n1)
ls.append(m1)
ls.append(h1)
def matrixMultiPly (a, b) :
    c1=[]
    c2=[]
    c3=[]
    c=[]
    for i in range(len(a)):
        r=a[0][0]*b[0][i]+a[0][1]*b[1][i]+a[0][2]*b[2][i]
        c1.append(r)
    for i in range(len(a)):
        r=a[1][0]*b[0][i]+a[1][1]*b[1][i]+a[1][2]*b[2][i]
        c2.append(r)
    for i in range(len(a)):
        r=a[2][0]*b[0][i]+a[2][1]*b[1][i]+a[2][2]*b[2][i]
        c3.append(r)
    c.append(c1)
    c.append(c2)
    c.append(c3) 
    return c
    

print(matrixMultiPly(lst,ls)[0])
print(matrixMultiPly(lst,ls)[1])
print(matrixMultiPly(lst,ls)[2])
