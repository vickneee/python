# \u2660 = ♠ Spade
# \u2663 = ♣ Club
# \u2665 = ♥ Heart
# \u2666 = ♦ Diamond

Rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Suit = ['♠', '♣', '♥', '♦']

OutputFilePath = "BlackJack.txt"
ofh = open(OutputFilePath, "w", encoding='utf-8')

for s in Suit:
    for r in Rank:
        Card = r + s + "\n"
        ofh.write(Card)
