def solve(s):
    words = s.split(' ')
    new = ' '.join([word.capitalize() for word in words])
    print(new)


solve('hello   world  lol')
