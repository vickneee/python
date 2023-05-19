html_code = """<!DOCTYPE html>
<html lang='fi'>
<head>
    <title>TableOfCountries</title>
    <style>
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 20px;
        }
        table {
            width: 800px;
        }
    </style>
</head>
<body>
    <h1>HTML sivu on tehty kokonaan Pythonilla!</h1>
    <table>
        <thead>
            <tr>
                <th>Country</th>
                <th>Capital</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Finland</td>
                <td>Helsinki</td>
            </tr>
            <tr>
                <td>France</td>
                <td>Paris</td>
            </tr>
        </tbody>
    </table>
    <h1>Taulujen viivat helpottavat taulun hahmottamista.</h1>
</body>
</html>
"""

with open("TableOfCountries-1.html", "w") as file:
    file.write(html_code)

print("HTML file generated: TableOfCountries-1.html")
