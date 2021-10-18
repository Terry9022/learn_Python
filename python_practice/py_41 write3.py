f1=open('../app/math_list.csv','r',encoding='big5')
txt1=f1.readlines()
f1.close()
f1=open('../app/english_list.csv','r',encoding='big5')
txt2=f1.readlines()
f1.close()
set1=set()
set2=set()
for i in range(len(txt1)):
    txt1[i]=txt1[i].strip().split(',')
for i in range(len(txt2)):
    txt2[i]=txt2[i].strip().split(',')              
for i in range(1,len(txt1)):
    set1.add(txt1[i][0])
for i in range(1,len(txt2)):
    set2.add(txt2[i][0])
a=set1.intersection(set2)
b=set1.union(set2)
c=set1-set2
d=set2-set1
e=b-a

a=list(a)
a.sort()
print(a)
e=list(e)
e.sort()
print(e)

c=list(c)
c.sort()
print(c)
d=list(d)
d.sort()
print(d)

b=list(b)
b.sort()
print(b)
