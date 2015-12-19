output = []
for value in range(10):
    if value > 5:
        output.append(str(value))
print output

# python provides a way to flat the four lines
# of code into just single one line.

output = [str(value) for value in range(10) if value > 5]


# consider the following situation
min([value for value in range(10) if value > 5])
# the comprehension returns a full list, only to
# have it thrown away when min() processes the values
# python provides a different option: generator expression.
gen = (value for value in range(10) if value > 5)
