#### set

# initialization
str_a = 'eggs'
print set(str_a)
print {'s', 'e', 'e', 'g'}

# add
print "s = set(str_a)"
s = set(str_a)
print "s.add('a')"
s.add('a')
print s
print "s.add('e')"
s.add('e')
print s

# update
print "s.update({1, 2, 3, 4})"
s.update({1, 2, 3, 4})
print s

# remove: raise exception if key not found
print "s.remove(1)"
s.remove(1)
print s

# discard: raise no exception if key not found
print "s.discard(2)"
s.discard(2)
print s

# pop
print "s.pop()"
s.pop()
print s

# clear
print "s.clear()"
s.clear()
print s

# union: the original set will not be changed
print "{1, 2, 3} | {4, 5, 6}"
print {1, 2, 3} | {4, 5, 6}

print "{1, 2, 3}.union({4, 5, 6})"
print {1, 2, 3}.union({4, 5, 6})

# intersection
print {1, 2, 3, 4, 5} & {4, 5, 6, 7, 8}
print {1, 2, 3, 4, 5}.intersection({4, 5, 6, 7, 8})

# difference
print {1, 2, 3, 4, 5} - {2, 4, 6}
print {1, 2, 3, 4, 5}.difference({2, 4, 6})

# symmetric_difference
print {1, 2, 3, 4, 5} ^ {4, 5, 6}
print {1, 2, 3, 4, 5}.symmetric_difference({4, 5, 6})

# subset and superset
{1, 2, 3}.issubset({1, 2, 3, 4, 5})
{1, 2, 3}.issuperset({1, 2, 3, 4, 5})
