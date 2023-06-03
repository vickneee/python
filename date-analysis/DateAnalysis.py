import datetime
from MyFunctions import InsertTr

htmlS = "<html>\n"
htmlE = "</html>\n"
tableS = "<table>\n"
tableE = "</table>\n\n"
trs = "<tr>\n"
tre = "</tr>\n"
ths = "<th>\n"
the = "</th>\n"
tab = "\t"
HeadAndLink = '''
<head>
    <link rel="stylesheet" href="DateAnalysis.css">
</head>\n
'''
OutputFilePath = "index.html"
ofh = open(OutputFilePath, "w")

d = datetime.datetime.now()

# F = Full, S = Short, N = Number
YearF = str(d.strftime("%Y"))
MonthS = str(d.strftime("%b"))
MonthF = str(d.strftime("%B"))
WeekDS = str(d.strftime("%a"))
WeekDF = str(d.strftime("%A"))
WeekDN = str(d.strftime("%w"))
DayOfMonth = str(d.strftime("%d"))

h = "DateAnalysis for " + str(d)
h_f = f"{h:^75}"  # ^ = Centered ###!!!!
dashLine = f'{"-"*75}'

# Writing to display
print()
print(dashLine)
print(h_f)
print(dashLine)
print(f"  {'Directive':18}{'Description':43}{'Value':25}")
print(dashLine)
print(f"  {'%Y':18}{'Year, full version':43}{YearF:25}")
print(f"  {'%b':18}{'Month name, short version':43}{MonthS:25}")
print(f"  {'%B':18}{'Month name, full version':43}{MonthF:25}")
print(f"  {'%d':18}{'Day of month 01-31':43}{DayOfMonth:25}")
print(f"  {'%a':18}{'Weekday, short version':43}{WeekDS:25}")
print(f"  {'%A':18}{'Weekday, full version':43}{WeekDF:25}")
print(f"  {'%w':18}{'Weekday as a number 0-6, 0 is Sunday':43}{WeekDN:25}")
print(dashLine)
print(dashLine)
print()

# Writing to file
ofh.write(htmlS)
ofh.write(HeadAndLink)
ofh.write(tableS)
InsertTr(ofh, "th", 3, h)
InsertTr(ofh, "td", "Directive", "Description", "Value")
InsertTr(ofh, "td", "%Y", "Year, full version", YearF)
InsertTr(ofh, "td", "%b", "Month name, short version", MonthS)
InsertTr(ofh, "td", "%B", "Month name, full version", MonthF)
InsertTr(ofh, "td", "%d", "Day of month 01-31", DayOfMonth)
InsertTr(ofh, "td", "%a", "Weekday, short version", WeekDS)
InsertTr(ofh, "td", "%A", "Weekday, full version", WeekDF)
InsertTr(ofh, "td", "%w", "Weekday as a number 0-6, 0 is Sunday", WeekDN)
ofh.write(tableE)
ofh.write(htmlE)
