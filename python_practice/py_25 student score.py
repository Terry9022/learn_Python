lst=[]
for j in range(5):
    n=input().split()
    for i in range(len(n)):
         n[i]=eval(n[i])
    lst.append(n)

b=0
t=0
c=0
s=0
for i in range(5):
    print('student',i+1)
    print(' 1:',lst[i][0])
    print(' 2:',lst[i][1])
    print(' 3:',lst[i][2])
    a=lst[i][0]+lst[i][1]+lst[i][2]
    print(' sum:',a)
    
    c=a/3
    print(' avg: %.2f'%(c))
    b=b+a
    if c>t:
        t=c
        s=s+1
    
print('total:',b,end="")
print(', avg: %.2f'%(b/15))
print('highest avg: student',s,end="")
print(': %.2f'%(t))

