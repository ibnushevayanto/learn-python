from replit import clear

print("Welcome to the secret auction program.")
bidder_list = []

def getWinnerBid(biddersList):
    theHighestBidder = None

    for bidder in biddersList:
        if theHighestBidder:
            if bidder["bid"] > theHighestBidder["bid"]:
                theHighestBidder = bidder
        else:
            theHighestBidder =  bidder   

    print(f"The Winner is {theHighestBidder['name']} with a bid of ${theHighestBidder['bid']}")

while True:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    data = {"name": name, "bid": bid }
    bidder_list.append(data)

    isAnyOtherBidder = input("Are they any other bidders? Type 'yes' or 'no': ").lower()

    if isAnyOtherBidder != 'yes':
        break
    else:
        clear()

getWinnerBid(bidder_list)
    