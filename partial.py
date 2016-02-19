import functools

int2 = functools.partial(int, base=2)
print(int2('10101001010100101001010101011100101'))
