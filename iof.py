# Copyright (C) 2020 Daniel Efimenko
#

n, m = map(int, input().split())

warriors = [i + 1 for i in range(n)]
next_to_kill = m - 1

while True:
    del warriors[next_to_kill % len(warriors)]
    if len(warriors) == 1:
        break
    next_to_kill += m

print(warriors)
