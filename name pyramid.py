x=input("enter your name:-")
y=list(x)
n=len(y)-1
m=1
for i in y:
    print(n*" ",i*m)
    n=n-1
    m=m+2