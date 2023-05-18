import random
from MyFunctions import SetValues, CalculateValue, PrintCard
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

Cards = []
Deck = []
InputFilePath = "BlackJack.txt"
ifh = open(InputFilePath, "r", encoding="utf-8")
for line in ifh:
    Cards.append(line.strip())
ifh = open(InputFilePath, "r", encoding="utf-8")
for line in ifh:
    Deck.append(line.strip())
UserCards = []
Aces = 0
Values = []
MyCards = []
NCards = 0
User = 0
Prompt = "Enter = Get a New Card, P = Pass, S = Stop: "
UserSum = 0  # Initialize UserSum here
while True:
    Choice = input(Prompt).upper()
    if Choice == "S":
        quit()
    if Choice == "P":
        pass
    elif Choice == "":
        random.shuffle(Deck)
        c = Deck[0]
        UserCards.append(c)
        NCards += 1
        (Values, Aces) = SetValues(c, Aces, Values)
        for c in UserCards:
            T = PrintCard(c)
        UserSum = CalculateValue(NCards, Aces, Values)
        if UserSum > 21:
            print(Fore.RED + Style.BRIGHT + str(UserSum))
        else:
            print(Fore.BLUE + Style.BRIGHT + str(UserSum))
        if UserSum == 21:
            print("BlackJack")
            Deck = Cards
            UserCards = []
            Aces = 0
            Values = []
            MyCards = []
            NCards = 0
            continue
        elif UserSum > 21:
            print("You lose")
            Deck = Cards
            UserCards = []
            Aces = 0
            Values = []
            MyCards = []
            NCards = 0
            continue
        else:
            continue
    else:
        print("Unknown choice")
        continue
    Deck = Cards
    UserCards = []
    Aces = 0
    Values = []
    MyCards = []
    NCards = 0
    while True:
        random.shuffle(Deck)
        MyCards.append(Deck[0])
        c = Deck[0]
        (Values, Aces) = SetValues(c, Aces, Values)
        for c in MyCards:
            T = PrintCard(c)
        MySum = CalculateValue(NCards, Aces, Values)
        if MySum > 21:
            print(Fore.RED + Style.BRIGHT + str(MySum))
        else:
            print(Fore.BLUE + Style.BRIGHT + str(MySum))
        if MySum > 21:
            print("You win")
            Deck = Cards
            UserCards = []
            Aces = 0
            Values = []
            MyCards = []
            NCards = 0
            break
        elif MySum > UserSum:
            print("You lose")
            Deck = Cards
            UserCards = []
            Aces = 0
            Values = []
            MyCards = []
            NCards = 0
            break
        else:
            continue
