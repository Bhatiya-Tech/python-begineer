inp=input("enter a line :")
length=len(inp)
digitcount=alphacount=spacecount=specialcount=0
for i in inp:
    if i.isdigit()==True:
        digitcount+=1
    elif i.isalpha()==True:
        alphacount+=1
    elif i.isspace():
        spacecount+=1
    else:
        specialcount+=1
print("no of digits= ",digitcount)
print("no of alphabet= ",alphacount)
print("no of spaces= ",spacecount)
print("no of special characters(#,$,@ etc..)= ",specialcount)
