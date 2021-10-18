n=input()
m=input()
f1=open("../app/%s"%n,"r")
txt1=f1.readlines()
f1.close()
f2=open("../app/%s"%m,"r")
txt2=f2.readlines()
f2.close()
lst=[]
hlst=[]
t=-99999999999
h=-1
for i in range(len(txt1)):
    txt1[i]=(txt1[i].strip().split(','))
for i in range(len(txt1)):
    txt2[i]=(txt2[i].strip().split(','))
  
for i in range(1,len(txt1)):
    txt1[i][1]=eval(txt1[i][1])
for i in range(1,len(txt2)):
    txt2[i][1]=eval(txt2[i][1])
    c=txt2[i][1]-txt1[i][1]
    lst.append(c)
for i in range(len(lst)):
    if lst[i]>t:
        t=lst[i]
b=lst.count(t)
if b >1:
    for i in range(b):
        
        h=lst.index(t,h+1)
        a=h+1
        hlst.append(a)
       
    for i in range(len(hlst)):
        hlst[i]=txt2[hlst[i]][0]
    hlst=" & ".join(hlst)
    
    print('Dark Horse: '+hlst)
    print('%.1f Points Progress'%t)    
          
else:        
    h=lst.index(t)+1
    
    print('Dark Horse: '+str(txt1[h][0]))
    print('%.1f Points Progress'%t)
