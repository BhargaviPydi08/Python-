logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

print("Welcome to secret auction!!")

def find_highest_bidder(bidding_dictionary):
    for bidder in bidding_dictionary:
        winner = ""
        highest_bid = 0
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
        #or use max() function - max(bidding_dictionary, key = bidding_dictionary.get)
    print(f"The winner is {winner} with a bid of {highest_bid}")

#comparing bids to find the highest bid

bids = {}

continue_bidding = True

#If new bids are to be added

while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'Yes' or 'No'.\n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*20)

        # or just use , clear()

        








