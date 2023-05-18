Capital = {
    'Finland': 'Helsinki',
    'Sweden': 'Stockholm',
    'Norway': 'Oslo',
    'Denmark': 'Copenhagen'
}
print(Capital)

Sanakirja = {'kirja': ['book', 'libro', 'libro'],
             'kurkku': [('cucumber', 'cetrilo', 'pepino'),
                        ('throat', 'gola', 'garanta')],
             'pala': ['piece', 'pezzo', 'pieza'],
             'ruoka': ['food', 'cibo', 'comida'],
             'yksi': ['one', 'uno', 'uno']}

x = Sanakirja.get("kurkku")
print(x)

a = "kurkku"
x = Sanakirja.get(a)
print(x)

print(Sanakirja)
