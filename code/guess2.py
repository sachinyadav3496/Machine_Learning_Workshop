from random import randint

c = randint(1,50)
for var in range(1,6) :
    u = int(input("Your guess : "))
    if u < c : 
        print("Be Big Think Big")
    elif u > c  : 
        print("Be in limits and think lower")
    else : 
        print("You have won the game ")
        break
    if var == 5 : 
        print("You such a looser : ")
        print("computer guess was : ",cq

