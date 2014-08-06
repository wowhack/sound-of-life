def read(fp):
  ls = []
  alive = set()
  with open(fp) as f:
    # Ignore all comments
    # Remove line endings
    ls = map(lambda l: l.strip(), filter(lambda l: l[0] != '#', f.readlines()))


  for yi, l in enumerate(ls):
    for xi, c in enumerate(l):
      if c == '*':
        alive.add((xi, xy))

  return alive
