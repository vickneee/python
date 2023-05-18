InputFilePath = "DataQualityInput5.txt"

ifh = open(InputFilePath, "r")
List = []
for line in ifh:
    if line == "\n":
        List.append(None)
    else:
        List.append(int(line))
print(List)
#
Total = len(List)
if Total == 0:
    print("No input")
    quit()
Null = 0
NonNull = 0
Duplicate = 0
Distinct = 0
NonUnique = 0
Unique = 0
#
for li in List:
    if li is None:
        Null = Null + 1  # kasvatetaan laskuri
T = []
for li in List:
    if li is not None:
        T.append(li)
List = T
print(List)
#
li1 = len(List)
NonNull = li1
if NonNull != 0:
    Set = set(List)
    li2 = len(Set)
    Distinct = li2
    Duplicate = li1 - li2
    for x in List:
        if List.count(x) == 1:
            Unique = Unique + 1
NonUnique = Distinct - Unique

DQA = "Data Quality Analysis"
T = "Total"
N = "  Null"
Nn = "  NonNull"
Dup = "    Duplicate"
Dis = "    Distinct"
Nunq = "      NonUnique"
Unq = "      Unique"

print()
print(f"{DQA:10}\t{'Count':>5}\t{'%':>5}")
print(f"{T:10}\t\t{Total:5d}\t{(Total / Total) * 100:5.0f}")

print(f"{N:10}\t\t{Null:5d}\t{(Null / Total) * 100:5.0f}")
print(f"{Nn:10}\t\t{NonNull:5d}\t{(NonNull / Total) * 100:5.0f}")
print(f"{Dup:10}\t\t{Duplicate:7d}\t{(Duplicate / Total) * 100:7.0f}")
print(f"{Dis:10}\t\t{Distinct:7d}\t{(Distinct / Total) * 100:7.0f}")
print(f"{Unq:10}\t\t{Unique:9d}\t{(Unique / Total) * 100:9.0f}")
print(f"{Nunq:10}\t\t{NonUnique:9d}\t{(NonUnique / Total) * 100:9.0f}")
print()

# Total = Null + NonNull
# NonNull = Duplicate + Distinct
# Distinct = NonUnique + Unique
