names = [
    {'first': 'lokesh', 'last': 'sharma'},
    {'first': 'Astha', 'last': 'verma'},
    {'first': 'jiu', 'last': 'rai'}
]

first_names = list(map(lambda x: x['first'], names))

print(first_names)
