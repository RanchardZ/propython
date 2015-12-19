print list(zip(range(3), reversed(range(5))))
# once the smallest sequence has been exhausted
# zip() simply stops looking through the others.

# it's useful when buiding the dictionary
keys = map(chr, range(97, 102))
values = range(1, 6)
print dict(zip(keys, values))
