ans=eval(input())
minval=1
maxval=100
while True:
    print(minval,"< ? <",maxval)
    g=eval(input())
    
    if minval<=g<=maxval:
        if g>ans:
            print("wrong answer, guess smaller")
            maxval=g
        elif g<ans:
            print("wrong answer, guess larger")
            minval=g
        else:
            print("bingo answer is",ans)
            break
    
