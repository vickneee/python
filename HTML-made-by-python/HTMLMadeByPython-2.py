doctype = "<!DOCTYPE html>\n"
htmls = "<html lang='fi'>\n"
heads = "<head>\n"
titles = "\t<title>"
toc = "TableOfCountries"
titlee = "</title>\n"
styles = "\t<style>\n"
CSS1 = "\t\ttable, th, td {\n\t\t\tborder: 1px solid black;\n\t\t}\n"
CSS2 = "\t\tth, td {\n\t\t\tpadding: 20px;\n\t\t}\n"
CSS3 = "\t\ttable {\n\t\t\twidth: 800px;\n\t\t}\n"
stylee = "\t</style>\n"
heade = "</head>\n"
bodys = "<body>\n"
h1s = "<h1>"
htmlpy = "HTML sivu on tehty kokonaan Pythonilla!"
h1e = "</h1>\n"
tables = "<table>\n"
theads = "\t<thead>\n"
trs = "\t<tr>\n"
ths = "\t\t<th>"
country = "Country"
thee = "</th>\n"
capital = "Capital"
tre = "\t</tr>\n"
theade = "\t</thead>\n"
tbodys = "\t<tbody>\n"
tds = "\t\t<td>"
finland = "Finland"
tde = "</td>\n"
helsinki = "Helsinki"
france = "France"
paris = "Paris"
tbodye = "\t</tbody>\n"
tablee = "</table>\n"
h2s = "<h2>"
taulujen = "Taulujen viivat helpottavat taulun hahmottamista."
h2e = "</h2>"
bodye = "</body>\n"
htmle = "</html>"

html1 = doctype + htmls + heads + titles + toc + titlee + styles + CSS1 + CSS2 + CSS3 + stylee + heade + bodys + h1s
html2 = htmlpy + h1e + tables + theads + trs + ths + country + thee + ths + capital + thee + tre + theade + tbodys
html3 = trs + tds + finland + tde + tds + helsinki + tde + tre + trs + tds + france + tde + tds + paris + tde
html4 = tre + tbodye + tablee + h2s + taulujen + h2e + bodye + htmle
html = html1 + html2 + html3 + html4

# print(html)

with open("TableOfCountries-2.html", "w") as file:
    file.write(html)

print("HTML file generated: TableOfCountries-2.html")
