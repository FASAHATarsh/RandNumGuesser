import random
chance = 0
x = random.randint(1,9)
while chance <=5:
    y = int(input("Enter number : "))
    if x == y:
        print("Congratulations!")
        break
    elif y<x:
        print("Guess was low!")
    else :
        print("Guess was high!")
    chance +=1
if not chance <=5:
    print("""You lose! 
The number was : """,x)