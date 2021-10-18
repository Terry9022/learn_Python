n=eval(input())
lst=[]
lst1=[]
t=0
s=0
for i in range(n):
    m=input().split()
    lst.append(m)

for i in range(len(lst)):
    lst[i][1]=eval(lst[i][1])
    a=lst[i][0]*lst[i][1]
    lst1.append(a)
lst1="".join(lst1)
for i in range(len(lst)):
    a=lst1.count((lst[i][0]))
    if a>t:
        t=a
        s=(lst[i][0])

print(s,t)
