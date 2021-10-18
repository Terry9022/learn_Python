n=eval(input()) #n=7
print(" "*(n-1)+"*")
b=n*2-1
c=b-2*(n-1)
d=c+6
e=2
f=n-2
for j in range(f):
        for i in range(c+e*j,d+e*j,2):
                a=int(((b)-i)/2)
                print(" "*a+"^"*i,end="")
                print()
g=int((n-3)/2)                
for k in range(n-2):               
        print(' '*(n-g-1)+'#'*(n-2))






















'''
for i in range(c,d,2):
        a=int(((b)-i)/2)
        print(" "*a+"^"*i,end="")
        print()
for i in range(c+e,d+e,2):
        a=int(((b)-i)/2)
        print(" "*a+"^"*i,end="")
        print()
for i in range(c+2*e,d+2*e,2):
        a=int(((b)-i)/2)
        print(" "*a+"^"*i,end="")
        print()
for i in range(c+3*e,d+3*e,2):
        a=int(((b)-i)/2)
        print(" "*a+"^"*i,end="")
        print()
for i in range(c+4*e,d+4*e,2):
        a=int(((b)-i)/2)
        print(" "*a+"^"*i,end="")
        print()
        '''
