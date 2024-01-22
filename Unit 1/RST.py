#Matteo Bascur & Arda Mumcu
#Jan 17, 2024
#Virtual Casino (RST)
import random
balance = 1000
print("\033[1;32mWelcome To Platinum Casino 💠")
def slots():
    print("Welcome to slots!🎰")
    print("")
    global balance
    stake_slots = int(input("Enter the amount you want to wager: $"))
    print("")
    balance = balance - stake_slots
    #Generates 9 random numbers and assigns them to variables (r1,r2,r3 etc)
    r1 = random.randint(1,9)
    r2 = random.randint(1,9)
    r3 = random.randint(1,9)
    r4 = random.randint(1,9)
    r5 = random.randint(1,9)
    r6 = random.randint(1,9)
    r7 = random.randint(1,9)
    r8 = random.randint(1,9)
    r9 = random.randint(1,9)
    #Generages the 9 numbers in a 3x3 grid and if 3 of the same numbers are in a row the users wagers gets multiplied by 100.
    print(f"⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠿⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢸⣿⣿⠛⠻⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇{r4}⠀⢸⡇{r5}⠀⢸⡇{r6}⠀⢸⣿⠀⢸⣿⣿⣤⣤⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇{r1}⠀⢸⡇{r2}⠀⢸⡇{r3}⠀⢸⣿⠀⢸⣿⣿⠈⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇{r7}⠀⢸⡇{r7}⠀⢸⡇{r9}⠀⢸⣿⠀⢸⣿⠁⢸⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⢸⣿⠀⢀⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣦⣼⣿⣿⣿\n⣿⣿⣿⣿⡿⠋⠀⣠⣤⣤⡄⢀⣤⣤⣤⡄⠀⠀⢠⣴⣶⣶⣤⡀⠙⢿⣿⣿⣿⣿\n⣿⣿⣿⡏⠀⠀⠚⠛⠛⠛⠁⠘⠛⠛⠛⠀⠀⠀⠈⠙⠛⠛⠉⠀⠀⠀⢹⣿⣿⣿\n⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿\n⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿\n")
    #Decides if you won or lost and changes your balance accordingly
    if r1 == r2 and r2 == r3 or r4 == r5 and r6 or r7 == r8 and r9:   
        print("YOU WON!🎰\n")
        stake_slots = stake_slots * 100
        balance = balance + stake_slots
    else:
        print("You lost🎰\n")
    print("Your new balance is: $" + str(balance))

def blackjack():
    # Sets balance to global variable so it can access it
    global balance
    print("Welcome to Blackjack! 🃏")
    print("")
    # Asks user for wager amount
    wagerBJ = int(input("Enter your wager amount: $"))
    print("")
    # Makes the blackjack deck 4 deck (All the cards x 4), all the 10s are face cards
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    # Shuffles the deck
    random.shuffle(deck)
    # Gives you and the dealer random cards and removes that card from the original deck
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    # If you do not get blackjack from the start, it tells you your hand and asks you if you want to hit or stand
    while sum(player_hand) < 21:
        print(f"Your hand: {player_hand}, Total: {sum(player_hand)}")
        print("")
        print(f"Dealer's hand: {dealer_hand}, Total: {sum(dealer_hand)}")
        print("")
        action = input("Do you want to hit or stand? ").lower()
        print("")
        # If you hit then it gives you the card from the deck and if you stand it stops
        if action == 'hit':
            player_hand.append(deck.pop())
        elif action == 'stand':
            break
    # If the dealer originally starts with a hand lower than 17, it is forced to get another card and it does that 
    while sum(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    print(f"Your hand: {player_hand}, Total: {sum(player_hand)}")
    print("")
    print(f"Dealer's hand: {dealer_hand}, Total: {sum(dealer_hand)}")
    print("")
    if sum(player_hand) > 21:
        print("Bust! You lose. 😢")
    elif sum(dealer_hand) > 21 or sum(player_hand) > sum(dealer_hand):
        print("Congratulations! You win. 🙂")
    elif sum(player_hand) == sum(dealer_hand):
        print("It's a tie. 🙂")
    else:
        print("You lose. 😢")
    if sum(player_hand) > 21:
        balance = balance - wagerBJ
    elif sum(dealer_hand) > 21 or sum(player_hand) > sum(dealer_hand):
        balance = balance + wagerBJ
    else:
        balance = balance - wagerBJ
    print("")
    print("")

def roulette():
    # Makes the balance the global variable of balance
    global balance
    print("Welcome to Roulette!😁")
    print("")
    # Asks for wager amount 
    wager_roulette = int(input("Enter your wager amount: $"))
    print("")
    # Asks for bet type
    bet_type = input("Choose a bet type (red, black, odd, even, number): ").lower()
    print("")
    # If bet is number then asks for number
    if bet_type == 'number':
        number_bet = int(input("Choose a number (0-36): "))
        print("")
    else:
        number_bet = None
    # Makes the roulette wheel and choses the winning number
    wheel = list(range(37))
    winning_number = random.choice(wheel)

    print(f"Spinning the wheel... The winning number is: {winning_number}")
    print("")
    # Outputs and changes your balance based on if you have won or lost
    if bet_type == 'number' and number_bet == winning_number:
        print("Congratulations! You win!😁")
    elif bet_type == 'red' and winning_number % 2 == 1:
        print("Congratulations! You win!😁")
    elif bet_type == 'black' and winning_number % 2 == 0:
        print("Congratulations! You win!😁")
    elif bet_type == 'odd' and winning_number % 2 == 1:
        print("Congratulations! You win!😁")
    elif bet_type == 'even' and winning_number % 2 == 0:
        print("Congratulations! You win!😁")
    else:
        print("Sorry, you lose. Try again!😞")
    print("")
    if bet_type == 'number' and number_bet == winning_number:
        balance = balance + wager_roulette
    elif bet_type == 'red' and winning_number % 2 == 1:
        balance = balance + wager_roulette
    elif bet_type == 'black' and winning_number % 2 == 0:
        balance = balance + wager_roulette
    elif bet_type == 'odd' and winning_number % 2 == 1:
        balance = balance + wager_roulette
    elif bet_type == 'even' and winning_number % 2 == 0:
        balance = balance + wager_roulette
    else:
        balance = balance - wager_roulette
    

def main():
    global balance
    while True:
        if balance <= 0:
            print("Thanks for playing! You have lost all your money 😭")
            break
        #Main menu, brings user to their desired game if they enter the corresponding number and changes text color to green
        print("\n (1) BlackJack 🃏\n (2) Roulette 💸\n (3) Slots 🎰\n (4) Rules ❓\n (5) Quit❌")
        print("")
        # States users balance every time a game ends
        print("Your balance is: $" + str(balance))
        print("")
        # Asks user for the game they want to play in the casino
        final_balance = balance - 1000
        choice_main = input("Enter the number of the game you want to play: ")
        # Converts their answer to an integer
        choice_main = int(choice_main)
        print("\n\n")
        # Whatever the person chooses it calls the function to go to their chosen game
        if choice_main == 1:
            blackjack()
        elif choice_main ==2:
            roulette()
        elif choice_main == 3:
            slots()
        elif choice_main == 4:
            rules()
        elif choice_main == 5 and final_balance < 1000:
            print("Thanks for playing! Goodbye. You have won $" + str(final_balance))
            break
        else:
            # Game does not run if user does not enter a proper answer
            print("Invalid choice. Please enter a number between 1 and 5.")
#Defines rules as a function and prints them when it is called
def rules():
    print("Welcome to Platinum Casino!\n\nBlackjack\nA computer will generate 2 random cards 1-11. The goal of the game is to get as close to 21 as can without going over because if you go over you bust and lose. The dealer/computer has to keep pulling cards until it gets to any number from 17-21. You can hit to get another card or stand to stay at the same number that your cards add up to.\n\nSlots\nWelcome to slots, the game is very simple and for the most part it is luck based, you will enter your stake/wager and then the computer will 3 lines of 3 numbers in each, if 3 in the line are the same then you will win 100 times the amount that you wagered but if they are not then you will lose your wager.\n\nRoulette\nIn this game you enter first what you want to bet on, you have the choice to bet on either an odd/even numbers/ a specific number (0-36), or you can bet on a color, you can bet on red, or black which both appear 18 times on the board or if you are feeling lucky you can bet on green which only appears on the board once but has a much greater reward.\n\nThank you for reading and best of luck! 🍀")
    print("")
#Allows program to run and prevents user from encountering errors
if __name__ == "__main__":
    main()