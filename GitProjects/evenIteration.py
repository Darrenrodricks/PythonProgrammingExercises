# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,
# 7,8,9,10).
a = (1,2,3,4,5,6,7,8,9,10)
b = list()
for values in a:
    if values % 2 == 0:
        b.append(values)

print(tuple(b))
        