n=eval(input())
if not 1<=n<=99999:
    print("out of range")
    exit(0)   
a=n//10000
b=(n//1000)%10
c=(n//100)%10
d=(n//10)%10
e=n%10
y=[a,b,c,d,e]
intab=("123456789")
outtab=("壹貳參肆伍陸柒捌玖")
transtab=str.maketrans(intab,outtab)
z=str(y).translate(transtab)
print("%s萬%s仟%s佰%s拾%s元整"%(z[1],z[4],z[7],z[10],z[13]))    

