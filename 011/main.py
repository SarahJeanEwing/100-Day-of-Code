import os
import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pick_card_and_adjust_score(score, hand):
    card = random.choice(cards)
    hand.append(card)
    score += card
    if score > 21:
        if 11 in hand:
            x = hand.index(11)
            hand[x] = 1
            score -= 10
    return score

def compare_score(player_current_score, dealer_current_score):
    if player_current_score == dealer_current_score:
        return "Draw 🙃"
    elif dealer_hand == [10, 11]:
        return "Lose, opponent has Blackjack 😱"
    elif player_hand == [10, 11]:
        return "Win with a Blackjack 😎"
    elif player_current_score <= 21 and dealer_current_score > 21:
        return "Opponent went over. You win 😁"
    elif dealer_current_score <= 21 and player_current_score < dealer_current_score:
        return "You lose 😤"
    elif player_current_score > 21:
        return "You went over. You lose 😭"
    elif player_current_score <= 21 and dealer_current_score < player_current_score:
        return "You win 😃"
    


more = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while more == "y":
    player_hand = []
    dealer_hand = []
    player_current_score = 0
    dealer_current_score = 0
    os.system('clear')
    print(art.logo)

    for _ in range(2):
        player_current_score = pick_card_and_adjust_score(player_current_score, player_hand)
        dealer_current_score = pick_card_and_adjust_score(dealer_current_score, dealer_hand)
        
    print(f"    Your cards: {player_hand}, current score: {player_current_score}")
    print(f"    Dealer's first card: {dealer_hand[0]}")
    if player_current_score == 21:
        game_over = True
    else:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        game_over = False
    while not game_over:
        while another_card == "y":
            print(player_hand)
            if another_card == "y":
                player_current_score = pick_card_and_adjust_score(player_current_score, player_hand)
                print(f"    Your cards: {player_hand}, current score: {player_current_score}")
                print(f"    Dealer's first card: {dealer_hand[0]}")
    
                if player_current_score >= 21:
                    game_over = True
                    another_card = "n"
                else:
                    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        
        game_over = True
    
    while dealer_current_score < 17 and player_current_score <= 21:
        dealer_current_score = pick_card_and_adjust_score(dealer_current_score, dealer_hand)

    print(f"   Your final hand: {player_hand}, final score: {player_current_score}")
    print(f"   Dealer's final hand: {dealer_hand}, final score: {dealer_current_score}")
   
    player_hand.sort()
    dealer_hand.sort()
    print(compare_score(player_current_score, dealer_current_score))

    
    
    more = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
os.system('clear')
print(art.logo)
print("Thanks for playing!")        