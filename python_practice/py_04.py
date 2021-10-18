x=eval(input())
if x == 1:
    y=eval(input())
    if 0<=y<=100:
        if y>=60:
            print("pass")
        else:
            print("fail")
    else:
        print("score error")
elif  x==2:
    y=eval(input())
    if 0<=y<=100:
        if y>=70:
            print("pass")
        else:
            print("fail")
    else:
        print("score error")
else:
    print("roll error")       

