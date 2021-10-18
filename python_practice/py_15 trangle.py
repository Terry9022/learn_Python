a=eval(input())
b=eval(input())
c=eval(input())
if a+b>c and a+c>b and b+c>a:
    print("True")
else:
    print("False")
    exit()
if (a**2 + b**2 )== (c**2) or (a**2 + c**2) == (b**2) or (c**2 + b**2) ==(a**2):
    print("Right Triangle")
else:
    print("Non-Right Triangle")
