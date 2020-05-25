

if __name__ == '__main__':
    max_len = int(input())
    z = []
    for i in range(int(input())):
        z.append(int(input()))
    k = 0
    while 1 in z:
        start = z.index(1)
        end = start + max_len
        for i in range(start, end):
            z[min(i, len(z) - 1)] = 0
        k += 1
    print(k)
