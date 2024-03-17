def my_numbers():
    a = 1
    while True:
        yield a
        a += 1


mygen = my_numbers()
print(next(mygen))
print(next(mygen))

r = range(0, 1000000, 1000)
print(r[1:10])
