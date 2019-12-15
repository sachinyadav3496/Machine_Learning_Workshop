from random import randint

comGuess = randint(1,50)

counter = 1

while counter <= 5 : 
    userGuess =  int(input("Your Guess (1,50): "))
    if userGuess < comGuess : 
        print("Be big think Big")
    elif userGuess > comGuess : 
        print("Be in Limits Think Lower")
    else : 
        print("Correct You have won the game ")
        break 
    if counter == 5 : 
        print("You such a looser !!")
        print("Computer Guess was ",comGuess)
    counter += 1
