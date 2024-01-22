# Arda Mumcu
# January 8th, 2024 
# This is an assignment on the game of pig
print("Welcome to the game of pig")
print("")
total = 0
final_total = 0
import random
turns = 1
print("Turn 1")
while True:
    
    roll = random.randint(1,6)
    print("You rolled a " + str(roll))
    if roll >= 2:
        total += roll
    print("This round you have: " + str(total))
    bank = input("Would you like to roll or bank? ")
    if bank == "bank":
        print("Your total for this round is: " + str(total))
    if bank == "roll":
        turns += 1
    if bank == "bank":
        turns = 0
    if bank == "bank":
        total += final_total
    if bank == "bank":
        total += final_total
        total = 0
    if final_total >= 100:
        break
    print("")
    if bank == "roll":
        print("Turn " + str(turns))
    if roll == 1:
        print("You lose this round")
        print("Your total for this round is zero")
print("")
if final_total >= 100:
    print("You win!")