x={'A':10,'J':18,'S':26,
 'B':11,'K':19,'T':27,
 'C':12,'L':20,'U':28,
 'D':13,'M':21,'V':29,
 'E':14,'N':22,'W':32,
 'F':15,'O':35,'X':30,
 'G':16,'P':23,'Y':31,
 'H':17,'Q':24,'Z':33,
 'I':34,'R':25}
n=input()
if n[0].isalpha() and n[1:10].isdigit() and len(n)==10:
    n=n.upper()
    n=list(n)
    n[0]=x[n[0]]
    for i in range(len(n)):
        n[i]=int(n[i])
    n[0]=str(n[0])
    n.insert(1,n[0][1])
    n.insert(1,n[0][0])
    n.remove(n[0])
    for i in range(len(n)):
        n[i]=int(n[i])
    a=n[0]*1 +n[1]*9+ n[2]*8 +n[3]*7 +n[4]*6 +n[5]*5+ n[6]*4 +n[7]*3 +n[8]*2 +n[9]*1 +n[10]*1
    if (a)%10==0:
        print("real")
    else:
        print("fake")
else:
    print("fake")
