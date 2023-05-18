import math
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def SetValues(c, Aces, Values):
    Ten = 10
    if len(c) == 3:
        Values.append(Ten)
    elif c[0] in ('J', 'Q', 'K'):
        Values.append(Ten)
    elif c[0] == 'A':
        Aces += 1
    else:
        Values.append(int(c[0]))
    return Values, Aces


def CalculateValue(NCards, Aces, Values):
    if NCards == 2:
        if Aces == 2:
            Sum = 21
        elif Aces == 1:
            if sum(Values) == 10:
                Sum = 21
            else:
                Sum = sum(Values) + (Aces * 11)
        else:
            Sum = sum(Values)
    else:
        if sum(Values) > 10:
            Sum = sum(Values) + (Aces * 1)
        else:
            if Aces > 0:
                Difference = 21 - sum(Values)
                NumberOf11 = Difference // 11
                if NumberOf11 == 1:
                    Sum = sum(Values) + 11 + ((Aces - 1) * 1)
                elif NumberOf11 == 2:
                    Sum = sum(Values) + (Aces * 11)
                else:
                    Sum = sum(Values) + (Aces * 1)
            else:
                Sum = sum(Values)
    return Sum


def PrintCard(Card):
    red = ['♦', '♥']
    if len(Card) == 3:
        print(Fore.WHITE + Style.BRIGHT + Card[0:2], end="")
        if Card[2] in red:
            print(Fore.RED + Style.BRIGHT + Card[2], end=" ")
        else:
            print(Fore.WHITE + Style.BRIGHT + Card[2], end=" ")
    else:
        print(Fore.WHITE + Style.BRIGHT + Card[0], end="")
        if Card[1] in red:
            print(Fore.RED + Style.BRIGHT + Card[1], end=" ")
        else:
            print(Fore.WHITE + Style.BRIGHT + Card[1], end=" ")
    return True
