import random

def compare_numbers(number, user_guess):
    ## your code here
    Cow = 0
    Bull = 0
    
    if len(user_guess) < 4:
        for i in range(4 - len(user_guess)):
            user_guess = "0"+user_guess

    if len(number) < 4:
        for i in range(4 - len(number)):
            number = "0"+number
            
    for n in number:
        if n in user_guess:
            Cow += 1

    for n in range(len(number)):
        if number[n] == user_guess[n]:
            Bull += 1
            Cow -= 1

    cowbull = [Cow, Bull]
    
    return cowbull

playing = True #gotta play the game
number = str(random.randint(0,9999)) #random 4 digit number
guesses = 0
print (number)

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
