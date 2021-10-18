n=eval(input())
import time
a=time.gmtime(n)
b=time.localtime(n)
c=time.strftime("%Y-%m-%d %H:%M:%S",a)
d=time.strftime("%Y-%m-%d %H:%M:%S",b)

print(c)
print(d)
