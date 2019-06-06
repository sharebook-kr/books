def myrange(start, end):
    cur = start
    while cur < end:
        yield  cur
        cur += 1

for i in myrange(0, 3):
    print(i)

