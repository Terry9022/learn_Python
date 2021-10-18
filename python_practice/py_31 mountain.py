n=eval(input())
m=input().split()
t=-99999999999999
s=999999999999999999
for i in range(len(m)):
    m[i]=eval(m[i])
    if m[i]>t:
        t=m[i]
    if m[i]<s:
        s=m[i]
a=m.index(t)+1
b=m.index(s)+1
        











print(a,t)
print(b,s)
