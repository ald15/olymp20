# @todo Доделать, тут ничего не понятно.

last_h = 0
length = 0

for i in range(int(input())):
    h = int(input())
    if h > last_h:
        length += 1
        last_h = h
