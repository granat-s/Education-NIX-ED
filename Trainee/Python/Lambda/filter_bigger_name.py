names = ['loesh', 'lassie', 'bob', 'to']

new = list(map(lambda name: f"your name is {name}",
               filter(lambda x: len(x) > 4, names)))

print(new)
