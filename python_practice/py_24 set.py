A = {"蘋果", "香蕉", "鳳梨", "芭樂"}
B = {"鳳梨", "蘋果", "水梨", "蓮霧"}
a1=input()
a2=input()
b1=input()
b2=input()
A.add(a1)
A.add(a2)
A.remove("蘋果")
B.add(b1)
B.add(b2)
B.remove("蓮霧")
c=A.intersection(B)
d=A.union(B)
e=A-B
f=B-A
g=d-c
A=list(A)
B=list(B)
c=list(c)
d=list(d)
e=list(e)
f=list(f)
g=list(g)
A.sort()
B.sort()
c.sort()
d.sort()
e.sort()
f.sort()
g.sort()

print('iA:',A)
print('iB:',B)
print('union:',d)
print('intersection:',c)
print('A diff B:',e)
print('B diff A:',f)
print('A xor B:',g)
