n = int(input())
y= int(n/12)
z= n%12
if z!=0:
    print(y,"dozen and",z)
else:
    print(y,"dozen")
