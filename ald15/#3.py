A, B, C, t = int(input()), int(input()), int(input()), 0

while True:

    A -= 1
    if A < 0:
        break
    else:
        t += 1

    B -= 1
    if B < 0:
        break
    else:
        t += 1

    C -= 1
    if C < 0:
        break
    else:
        t += 1

    B -= 1
    if B < 0:
        break
    else:
        t += 1

print(t)
