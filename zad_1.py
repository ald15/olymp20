

if __name__ == '__main__':
    a = int(input())
    n = int(input())
    if a < 0 and n > 0:
        a += n
        if a >= 0:
            a += 1
    elif a > 0 and n < 0:
        a += n
        if a <= 0:
            a -= 1
    else:
        a += n
    print(a)
