html_code = """<!DOCTYPE html>
<html lang='fi'>
<head>
    <title>Taulukko</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 100px;
            background-color: beige;
        }
        table, th, td {
            border: 1px solid black;
        }
        thead {
            background-color: #c4b0b0;
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
                <td>Estonia</td>
                <td>Tallinn</td>
            </tr>
             <tr>
                <td>Latvia</td>
                <td>Riga</td>
            </tr>
            <tr>
                <td>Lithuania</td>
                <td>Vilnius</td>
            </tr>
        </tbody>
    </table>
    <h2>Taulujen viivat helpottavat taulun hahmottamista.</h2>
</body>
</html>
"""

with open("TableOfCountries-1.html", "w") as file:
    file.write(html_code)

print("HTML file generated: TableOfCountries-1.html")
