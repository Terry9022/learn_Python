f1=open('../app/stores_old.csv','r',encoding="big5")
txt=f1.readlines()
f1.close()
for i in range(len(txt)):
    txt[i]=txt[i].strip().split(',')
for i in range(len(txt)):
    for j in range(len(txt[i])):
        if j==0 or j==3 or j==5 or j==6:          
            print(txt[i][j]+',',end='')
    print()
