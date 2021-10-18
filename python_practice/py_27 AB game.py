n=input()
n=list(n)

while True:
    A=0
    B=0
    m=input()
    m=list(m)
    for i in range(len(m)):
        if m[i]==n[i]:
            A+=1
        elif m[i] in n :
            
            B+=1
            
            
    print('%dA%dB'%(A,B))
    A=0
    B=0
    

    if m==n:
        print('You Win!')
        break



