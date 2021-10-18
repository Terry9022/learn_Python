x = eval(input())
y=x #瓶蓋
ans=x
z=y//4 #換得瓶子
while True:
    ans=ans+z #總共瓶子
    y=(y%4)+z #現在瓶蓋
    z=y//4 #換新瓶子
    if y==3:
        ans=ans+1
        break
    elif y<4:
        break
    else:
        continue
print(ans)
            
       

    
