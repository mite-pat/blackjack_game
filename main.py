############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
## Dealer with < 17 must take another card

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

from art import logo
import random

def final_score_message():
    '''Show message displaying cards and current score'''
    print(f"Your final hand: {player_cards}, final score: {current_score(player_cards)}")
    print(f"Computer's final hand: {cpu_cards}, final score: {current_score(cpu_cards)}")

# Get current score
def current_score(score_list):
    '''Calculate total score for user/cpus hand'''
    current_score = 0
    for x in range(len(score_list)):
        current_score += score_list[x]
    return current_score

# Prevent double 11 aces for both player and cpu
def initial_aces(card_list):
    '''Alters initial hand to make sure initial hand is not over 21'''
    if card_list[0] == 11 and card_list[1] == 11:
        card_list[1] = 1

def ace_picker(score_list):
    '''Decides when to pick 11 or 1 for ace, if 11 causes hand to go over 21 it will choose 1'''
    if current_score(score_list) > 11 and current_score(score_list) < 21 and score_list[-1] == 11:
        score_list[-1] = 11
    elif score_list[-1] == 11 and current_score(score_list) > 21:
        score_list[-1] = 1
    
def cpus_game(cpu_list):
    ''''Cpu will keep hitting until hand is > 18 and not blackjack'''
    while current_score(cpu_list) < 17 and current_score(cpu_list) != 21:
        cpu_cards.append(random.choice(cards))
        ace_picker(cpu_cards)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while True:
    player_cards = []
    cpu_cards = []
    play_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_choice == 'y':
        print(chr(27) + "[2J") # escape sequences to clear the screen
        print(logo)

        # Randomize starting hand
        for x in range(2):
            player_cards.append(random.choice(cards))
            cpu_cards.append(random.choice(cards))
        initial_aces(player_cards)
        initial_aces(cpu_cards)

        print(f"Your cards: {player_cards}, current score: {current_score(player_cards)}")
        print(f"Computer's first card: {cpu_cards[0]}")

        cpus_game(cpu_cards)
        
        # Add another card
        hit_flag = True
        another_card = ""

        while hit_flag:
            if current_score(player_cards) != 21:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                player_cards.append(random.choice(cards))
                ace_picker(player_cards)
                print(f"Your cards: {player_cards}, current score: {current_score(player_cards)}")
                print(f"Computer's first card: {cpu_cards[0]}")
                
                if current_score(player_cards) > 21:
                    hit_flag = False
                    final_score_message()
                    print("You went over. You lose 😤")
            else:
                hit_flag = False

                if current_score(player_cards) == 21 and current_score(cpu_cards) != 21:
                    final_score_message()
                    print("Win with a Blackjack 😎")
                elif current_score(cpu_cards) == 21 and current_score(player_cards) != 21:
                    final_score_message()
                    print("Lose, opponent has Blackjack 😱")
                elif current_score(cpu_cards) > 21 and current_score(player_cards) < 21:
                    final_score_message()
                    print("You win 😃")
                elif current_score(player_cards) > current_score(cpu_cards):
                    final_score_message()
                    print("You win 😃")
                elif current_score(player_cards) < current_score(cpu_cards):
                    final_score_message()
                    print("You lose 😤")
                else:
                    final_score_message()
                    print("Draw 🙃")

            another_card = ""
    else:
        break