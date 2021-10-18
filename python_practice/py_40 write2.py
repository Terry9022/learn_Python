f1=open('./stores_old.csv','r',encoding="big5")
txt=f1.readlines()
f1.close()

for i in range(len(txt)):
    txt[i]=txt[i].strip().split(',')

f2=open('‧／stores_new.csv','w',encoding='utf-8')
    
for i in range(len(txt)):
    for j in range(len(txt[i])):
        if j==0 or j==3 or j==5 or j==6:          
            f2.write(txt[i][j]+',')
    f2.write('\n')
f2.close()


f3=open('‧／stores_new.csv','r',encoding='utf-8')
txt1=f3.readlines()
f3.close()

for i in range(len(txt1)):
    txt1[i]=txt1[i].strip()
    print(txt1[i])
