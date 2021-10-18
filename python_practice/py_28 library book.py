n=input()
n=n.lower()
lst=[]
while True:
    m=input()
    if m=="q":
        break
    lst.append(m)
if n in lst:
    a=lst.index(n)+1
    print('Yes',a)
else:
    b=len(lst)
    print('No',b)




