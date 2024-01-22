# Arda Mumcu
# January 9th, 2024
# This is our second lab, where we will be creating our own quiz

# Setting the original score to 0
score = 0
# Greeting the user and setting the text color to green
print("\033[1;32m Hello, welcome to my quiz, in this quiz there will be 7 different questions that will test your knowledge. Do you think you have what it takes \U0001F92A? ")
print("")
# Asking the question and stating the answers
print("Question 1")
print("")
print("What is 8 x 13?")
print("")
print("(a) 98")
print("(b) 110")
print("(c) 104")
print("")
# Asking the user for their answer
answer1 = input("")
print("")
# If the answer is correct give them a point and tell them if they got it correct, if not tell them it was wrong
if answer1.upper() == 'C':
    print("Correct! \U0001F600")
else:
    print("Incorrect. That is a bad start \U0001F627")
if answer1.upper() == 'C':
    score += 1
print("")
print("")

print("Question 2")
print("")
# Asking the question
answer2 = input("Who won the 2022 World Cup? ")
print("")
# If the answer is correct give them a point and tell them if they got it correct, if not tell them it was wrong
if answer2.upper() == "ARGENTINA":
    print("Correct, wow nice knowledge \U0001F92A")
else:
    print("Incorrect, you'll get him next time \U0001F627")
if answer2.upper() == "Argentina":
    score +=1
print("")
print("")
print("Question 3")
print("")
try:
# Asking the question
    answer3 = int(input("What is 6x7? "))
    print("")
# If the answer is correct tell them if they got it correct, if not tell them it was wrong
    if answer3 == 42:
        print("Correct. Wow you are very good at math! \U0001F92A")
    else:
        print("Incorrect. Maybe math is not for you \U0001F62D")
    if answer3 == 42:
        score+=1
# If they do not enter a number tell them that they did not enter a number
except ValueError:
    print("")
    print("Incorrect. That's not a number silly \U0001F627")
# Give them another chance to answer
    print("")
    answer3_again = int(input("Try to enter your answer again: "))
    print("")
# If they get the answer right now give them a point and tell them if they got it right or wrong
    if answer3_again == 42:
        print("Correct. I knew you could do it \U0001F92A")
    else:
        print("Incorrect. You got it wrong again \U0001F62D")
# Add to their score if they get it right
    if answer3_again == 42:
        score+=1
print("")
print("")

print("Question 4")
print("")
# Asking the question and stating the answers
print("Who is the current president of the United States  ")
print("")
print("(a) Barrack Obama")
print("(b) Joe Biden")
print("(c) Donald Trump")
print("")
answer4 = input("")
print("")
# If the answer is correct give them a point and tell them if they got it correct, if not tell them it was wrong
if answer4.upper() == 'B':
    print("Correct! You must be from the United States \U0001F600")
else:
    print("Incorrect, it's ok if you are not American \U0001F627")
if answer4.upper() == 'B':
    score += 1
print("")
# Asking user if they have enjoyed the quiz so far and responding to them
enjoy = input("Are you enjoying this quiz so far? (yes/no) ")
print("")
if enjoy.upper() == "YES":
    print("Thank you for enjoying my quiz! \U0001F600")
else:
    print("Im sorry you have not liked it so far, hopefully it gets better \U0001F627!")
print("")
print("")

print("Question 5")
print("")
# Asking the question 
answer5 = input("What is the capital of Germany? ")
print("")
# If the answer is correct give them a point and tell them if they got it correct, if not tell them it was wrong
if answer5.upper() == "BERLIN":
    print("Correct, you are very good at geography \U0001F600!")
else:
    print("Incorrect, you might not be the best at geography \U0001F627")
if answer5.upper() == "BERLIN":
    score +=1
print("")
print("")

print("Question 6")
print("")
try:
# Asking the question
    answer6 = int(input("What is 12x11? "))
    print("")
# If the answer is correct give them a point and tell them if they got it correct, if not tell them it was wrong
    if answer6 == 132:
        print("Correct. Wow you are very good at math! \U0001F92A")
    else:
        print("Incorrect. Maybe math is not for you \U0001F62D")
    if answer6 == 132:
        score+=1
except ValueError:
# If they do not enter a number tell them that they did not enter a number
    print("")
    print("Incorrect. That's not a number silly \U0001F62D")
    print("")
# Giving them a chance to enter their answer again
    answer6_again = int(input("Try to put in your answer again: "))
    print("")
# If they get it right this time give them the point and tell them they got it right or wrong
    if answer6_again == 132:
        print("Correct. I knew you could do it \U0001F92A ")
    else:
        print("Wrong twice in a row! \U0001F62D")
    if answer6_again == 132:
        score+=1

print("")
print("")

# Asking the question and stating the answers
print("Question 7. This is the final question")
print("")
print("How many legs does a spider have?")
print("")
print("(a) 8")
print("(b) 10")
print("(c) 12")
print("")
answer7 = input("")
print("")
# If the answer is correct give them a point and tell them if they got it correct, if not tell them it was wrong
if answer7.upper() == 'A':
    print("Correct! You are so smart \U0001F600")
else:
    print("Incorrect, ending off poorly \U0001F62D")
if answer7.upper() == 'A':
    score += 1
print("")

# Calculate their average (percentage)
average = score / 7 * 100
# Round the average to 2 decimal places
average = round(average,2)
# Tell them how many they got write and what the average was
print("You finished! You scored a " + str(score) + " out of 7 and got a "+ str(average)+ "%.\n")
print("Hopefully you enjoyed this quiz and had a lot of fun \U0001F600!")