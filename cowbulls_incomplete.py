import random
cowbullcount = [0,0] # setting initial values for cows and bulls
def compare_numbers(number, user_guess):
    global cowbullcount #import this global variable
    cow_placeholder = cowbullcount[0] #set a placeholder for cow counts to detect a number out of the sequence
    bull_placeholder = cowbullcount[1] #set a placeholder for bull counts to detect a number out of the sequence
    for x in range(len(number)):
        if str(number[x]) == user_guess and str(number[cowbullcount[1]]) != user_guess:
            cow = cowbullcount[0]+1 #increment cow count by 1
            bull = cowbullcount[1] #keepig bull count at the original value (otherwise I can't return 2 values)
            print("\nThat Number exists in the sequence, but it's at a different place! Try Again!")
            break
        elif str(number[cowbullcount[1]]) == user_guess:
            bull=cowbullcount[1]+1 #increment bull count by 1
            cow = cowbullcount[0] #keepig cow count at the original value (otherwise I can't return 2 values)
            print("\nRight place, right number! onto the next number!")
            break
        else:
            bull = cowbullcount[1] # keeping both values the same because the number is out of the sequence
            cow = cowbullcount[0]
    if bull == bull_placeholder and cow == cow_placeholder:
        print("\nThat number isn't in the sequence! Try Again!")
    return cow, bull # returning the values


playing = True #gotta play the game
number = str(random.randint(1000, 9999)) #random 4 digit number
guesses = 0
#print(number) #leaving it in as a comment in case I need to debug this code again

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!: ")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number, user_guess)
    guesses += 1

    print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1] == 4:
        playing = False
        print("You won the game after " + str(guesses) + "guesses! The number was "+str(number))
        break #redundant exit
