import csv
from pprint import pprint
import mysql.connector
from tabulate import tabulate
mydb = mysql.connector.connect(
	host="localhost",
	user="BigData",
	password="BigData123,",
	database="BigData"
)

# Tenure = vakinainen virka
# Assistant Prof = Apulaisprofessori
# Associate Prof = Apulaisprofessori

Professor = []
InputFilePath = "Professor.txt"
with open(InputFilePath) as ifh:
	lines = csv.DictReader(ifh, delimiter='\t')
	for row in lines:
		row['Pid'] = int(row['Pid'])
		row['Years'] = int(row['Years'])
		Professor.append(row)
pprint(Professor)
for p in Professor:
	if (p['Title'] == 'Professor') or (p['Years']) > 6:
		p['Tenured'] = 'Y'
	else:
		p['Tenured'] = 'N'
pprint(Professor)


mycursor = mydb.cursor()
sql = "truncate Professor"
mycursor.execute(sql)
sql = "insert into Professor (Pid, Name, Title, Years, Tenured) values (%s, %s, %s, %s, %s)"
for p in Professor:
	val = (p['Pid'], p['Name'], p['Title'], p['Years'], p['Tenured'])
	mycursor.execute(sql, val)
mydb.commit()
sql = "select * from Professor"
mycursor.execute(sql)
mycolumns = mycursor.column_names
myresult = mycursor.fetchall()
print(tabulate(myresult, headers=mycolumns, tablefmt='psql'))
