# Define a function which can generate a list where the values are square of numbers between
# 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
def except_five():
    l = list()
    for i in range(1, 21):
        l.append(i ** 2)
    print(l[5:])

except_five()