lst=[]
while True:
    n=input()
    if n =="-1":
        break
    lst.append(n)
m=input()
t=-1
for i in range(len(lst)):
    if len(lst[i])>t:
        t=len(lst[i])
print(m*(t+2))        
for i in range(len(lst)):
    a=len(lst[i])
    print(m,end='')
    print(lst[i],end='')
    print(' '*(t-a),end='')
    print(m)
print(m*(t+2))

          

