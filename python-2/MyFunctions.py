import math


def Greeting(name):
    s = "Hello " + name
    return s


def LaskeYhteen(a, b):
    s = a + b
    return s


def IsPrime(n):
    Factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            Factors.append(i)
    if len(Factors) == 2:
        return [Factors, True]
    else:
        return [Factors, False]


def Summa(start, stop):
    summa = 0
    List = []
    for i in range(start, stop + 1):
        List.append(i)
        summa += i  # summa = summa + i
    return [List, summa]


def Area(shape, base=0, width=0, height=0, radius=0):
    # shape: t=triangle, r=rectangle, c=circle
    if shape == "T":
        area = base * height / 2
    elif shape == "R":
        area = width * height
    else:
        area = (radius ** 2) * math.pi
    return area


def InsertTr(ofh, tag, s=0, *argv):
    tab = "\t"
    eol = "\n"
    if s != 0:
        colspan = " colspan=" + str(s)
        tags = "<" + tag + colspan + ">"
    else:
        tags = "<" + tag + " >"
    tage = "</" + tag + "> "
    ofh.write("<tr>\n")
    ofh.write(tab)
    for data in argv:
        ofh.write(tags + data + tage)
    ofh.write(eol)
    ofh.write("</tr>\n")
