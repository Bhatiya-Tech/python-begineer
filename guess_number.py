import random
guess_no=random.randint(1,51)
for x in range(5):
    a=int(input("Guess a number between 1 to 50:= "))
    if a==guess_no:
        print("Congrulation")
        break
    elif a<guess_no:
        print("try again: Your number is small")
    else:
        print("try again: Your number is large")
print("Lucky Number:",guess_no)    

    
