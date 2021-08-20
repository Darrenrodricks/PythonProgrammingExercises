# Define a function which can print a dictionary where the keys are numbers between
# 1 and 3 (both included) and the values are square of keys.

def square():
    d = dict()
    d[0] = 1
    d[1] = 2 ** 2
    d[2] = 2 ** 2
    d[3] = 3 ** 2
    print(d)

square()