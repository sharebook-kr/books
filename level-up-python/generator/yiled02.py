def myrange(start, end):
    cur = start
    while cur < end:
        yield  cur
        cur += 1

g = myrange(0, 3)
print(type(g))

print(next(g))
print(next(g))
print(next(g))


