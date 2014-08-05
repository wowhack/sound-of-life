def read(file, x, y):
    ls = []
    with open(file) as f:
        # Ignore all comments
        # Remove line endings
        ls = map(lambda l: l.strip(), filter(lambda l: l[0] != '#D', f.readlines()))
    
    life = [[0] * x] * y

    for yi, l in enumerate(ls):
        for xi, c in enumerate(l):
            if c == '*':
                life[yi][xi]=1

    return life
