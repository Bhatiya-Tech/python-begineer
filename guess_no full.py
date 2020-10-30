import random
l=random.randint(1,21)
print("Guess the number between 1 to 20")
def inp():
    global a
    a=input("Enter the number=")
    y=a.isdigit()
    if y==True:
        print("valid entry :-)")
    else :
        print(" :-0 Enter valid no")
        inp()
for i in range(3):
    inp()
    a=int(a)
    if a>l:
        print("Your number is large")
    elif a==l:
        print("Congrulation ")
    else:
        print("Your number is small")

   
    
