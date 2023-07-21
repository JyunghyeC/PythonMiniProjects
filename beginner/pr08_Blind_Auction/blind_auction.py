import art

lst_bidder = {}


def auction(bidding):
    max_bid = 0
    winner = ""

    for i in lst_bidder:
        bid_amount = lst_bidder[i]
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = i

    print(f"The winner is {winner} with a bid of ${max_bid}")


should_end = False
print(art.logo)
print("Welcome to the secret auction program. ")

while not should_end:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : $"))
    lst_bidder[name] = bid

    add_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if add_bidder == "no":
        should_end = True
        auction(lst_bidder)
