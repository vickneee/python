import math


def Summa(start, stop):
    summa = 0
    List = []
    for i in range(start, stop + 1):
        List.append(i)
        summa += i  # summa = summa + i
    return [List, summa]