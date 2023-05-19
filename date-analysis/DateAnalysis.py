import datetime
from MyFunctions import InsertTr

htmls = "<html>\n"
htmle = "</html>\n"
tableS = "<table>\n"
tableE = "</table>\n"
trs = "<tr>\n"
tre = "</tr>\n"
ths = "<th>\n"
the = "</th>\n"
tab = "\t"
HeadAndLink = '''
<head>
    <link rel="stylesheet" href="DateAnalysis.css">
</head>
'''
OutputFilePath = "DateAnalysis.html"
ofh = open(OutputFilePath, "w")

d = datetime.datetime.now()

# F = Full, S = Short, N = Number
YearF = str(d.strftime("%Y"))
MonthS = str(d.strftime("%b"))
MonthF = str(d.strftime("%B"))
WeekDS = str(d.strftime("%a"))
WeekDF = str(d.strftime("%a"))
WeekDN = str(d.strftime("%w"))
DayOfMonth = str(d.strftime("%d"))

h = "DateAnalysis for " + str(d)
h_f = f"{h:^75}"  # ^ = Centered ###!!!!
dashline = f'{"-"*75}'

# writing to display
print()
print(dashline)
print(h_f)
print(dashline)
print(f"{'Directive':25}{'Description':40}{'Value':25}")
print(dashline)
print(f"{'%Y':25}{'Year, full version':40}{YearF:25}")
print(f"{'%b':25}{'Month name, short version':40}{MonthS:25}")
print(f"{'%B':25}{'Month name, full version':40}{MonthF:25}")
print(f"{'%d':25}{'Day of month 01-31':40}{DayOfMonth:25}")
print(f"{'%a':25}{'Weekday, short version':40}{WeekDS:25}")
print(f"{'%A':25}{'Weekday, full version':40}{WeekDF:25}")
print(f"{'%w':25}{'Weekday as a number 0-6, 0 is Sunday':40}{WeekDN:25}")

# writing to file
ofh.write(htmls)
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
ofh.write(htmle)
