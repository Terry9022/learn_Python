x={'P':'Pikachu','M':'Mickey Mouse','H':'Hello kitty'}
while True:
    n=input()
    if n=="-1":
        break
    if n in x:
        print(x[n])
    else:
        print(n,'does not exist. Enter a new one:')

        a=input()
        x[n]=a
