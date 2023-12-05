users = [
    {"username": 'samuel', "tweets": ["i love cake", "i am good"]},
    {"username": 'andy', "tweets": []},
    {"username": 'kumal', "tweets": ["India", "Python"]},
    {"username": 'sam', "tweets": []},
    {"username": 'lokesh', "tweets": ["i am good"]},
]

inactive_users = list(filter(lambda a: not a['tweets'], users))
print(inactive_users)
