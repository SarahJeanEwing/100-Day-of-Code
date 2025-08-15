import os
from art import logo

def find_highest_bidder(bids):
    highest_bidder = ""
    highest_bid = 0
    
    for bidder in bids:
        current_bid = bids[bidder]
        current_bidder = bidder
        if current_bid > highest_bid:
            highest_bid = current_bid
            highest_bidder = current_bidder
    
    os.system('clear')
    print(logo)
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

bids = {}
more_bidders = "yes"
while more_bidders == "yes":
    print(logo)
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    more_bidders = input("Are there any more bidders? Type 'yes' or 'no'. ")
    os.system('clear')
    bids[name] = bid
find_highest_bidder(bids)