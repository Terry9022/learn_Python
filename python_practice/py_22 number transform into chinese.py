x={'1':'壹','2':'貳'
   ,'3':'參','4':'肆',
   '5':'伍','6':'陸','7':'柒',
   '8':'捌','9':'玖','0':''}
n=input()
n=n.zfill(5)

a=int(n)
if not 1<=a<=99999:
    print('out of range')
    quit()
n=list(n)

for i in range(len(n)):
    n[i]=x[n[i]]

if 1<=a<=9:
    print('%s%s%s%s%s元整'%(n[0],n[1],n[2],n[3],n[4]))
elif 10<=a<=99:
    print('%s%s%s%s拾%s元整'%(n[0],n[1],n[2],n[3],n[4]))
elif 100<a<=999:
    print('%s%s%s佰%s拾%s元整'%(n[0],n[1],n[2],n[3],n[4]))
elif 1000<=a<=9999:
    print('%s%s仟%s佰%s拾%s元整'%(n[0],n[1],n[2],n[3],n[4]))
elif 10000<a<=99999:
    print('%s萬%s仟%s佰%s拾%s元整'%(n[0],n[1],n[2],n[3],n[4]))
elif a==10000:
    print('%s萬%s%s%s%s元整'%(n[0],n[1],n[2],n[3],n[4]))
elif a==100:
    print('%s%s%s佰%s%s元整'%(n[0],n[1],n[2],n[3],n[4]))
