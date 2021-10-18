n=input()
m=input()
f1= open('../app/%s'%n,'r')
txt1=f1.readlines()
f1.close()
f2=open('../app/%s'%m,"r")
txt2=f2.readlines()
f2.close()
lst=[]
for i in range(len(txt1)):
    txt1[i]=txt1[i].strip().split()
    
    for j in range(len(txt1[i])):
        lst.append(txt1[i][j])
    
for i in range(len(txt2)):
    txt2[i]=txt2[i].strip().split()
    
    for j in range(len(txt2[i])):
        lst.append(txt2[i][j])               
for i in range(len(lst)):
    lst[i]=eval(lst[i])
lst.sort()
for i in range(len(lst)):
    lst[i]=str(lst[i])

lst=' '.join(lst)
print(lst+' ')
